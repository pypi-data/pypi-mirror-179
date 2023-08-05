# ver.110 2022/02/04: 複数モータに対する同時入力追加
# ver.111 2022/04/08: Baud rateを指定可能に
# ver.112 2022/04/20: exitでトルクオフ、reboot追加
# ver.113 2022/04/25: baudrateの処理変更，出力の値


from enum import IntEnum, auto
from pip._internal import main as _main

try:
    import numpy as np
except ImportError:
    _main(['install', 'numpy'])
    import numpy as np

try:
    from dynamixel_sdk import *
except ImportError:
    _main(['install', 'dynamixel_sdk'])
    from dynamixel_sdk import *

class Dxlfunc:
    class Adrress(IntEnum):
        ModelNumber         = 0
        ModelInformation    = 2
        VersionOfFirmware   = 6
        ID                  = auto()
        BaudRate            = auto()
        ReturnDelayTime     = auto()
        DriveMode           = auto()
        OperatingMode       = auto()
        SecondaryShadowID   = auto()
        ProtocolVersion     = auto()
        HomingOffset        = 20
        MovingThreshold     = 24
        TemperatureLimit    = 31
        MaxVoltageLimit     = auto()
        MinVoltageLimit     = 34
        PWMLimit            = 36
        CurrentLimit        = 38
        AccelerationLimit   = 40
        VelocityLimit       = 44
        MaxPositionLimit    = 48
        MinPositionLimit    = 52
        Shutdown            = 63
        TorqueEnable        = auto()
        LED                 = auto()
        StatusReturnLevel   = 68
        RegisteredInstruction = auto()
        HardwareErrorStatus = auto()
        VelocityIGain       = 76
        VelocityPGain       = 78
        PositionDGain       = 80
        PositionIGain       = 82
        PositionPGain       = 84
        Feedforward2ndGain  = 88
        Feedforward1stGain  = 90
        BusWatchdog         = 98
        GoalPWM             = 100
        GoalCurrent         = 102
        GoalVelocity        = 104
        ProfileAcceleration = 108
        ProfileVelocity     = 112
        GoalPosition        = 116
        RealtimeTick        = 120
        Moving              = 122
        MovingStatus        = auto()
        PresentPWM          = auto()
        PresentCurrent      = 126
        PresentVelocity     = 128
        PresentPosition     = 132
        VelocityTrajectory  = 136
        PositionTrajectory  = 140
        PresentInputVoltage = 144
        PresentTemperature  = 146

    class operating_mode(IntEnum):
        current_control = 0
        velocity_control = auto()
        non = auto()
        position_control = auto()
        extended_Position_control = auto()
        current_base_position_control = auto()

    def __init__(self):
        self.portHandler = None
        self.packetHandler = PacketHandler(2.0)
        self.IDs = []
        self.Present_OperatingMode = -1
        self.one_byte_values = [self.Adrress.ID.value, self.Adrress.BaudRate.value, self.Adrress.ReturnDelayTime.value,
                                self.Adrress.DriveMode.value, self.Adrress.OperatingMode.value,
                                self.Adrress.SecondaryShadowID.value, self.Adrress.ProtocolVersion.value,
                                self.Adrress.TemperatureLimit.value, self.Adrress.Shutdown.value,
                                self.Adrress.TorqueEnable.value, self.Adrress.LED.value,
                                self.Adrress.StatusReturnLevel.value, self.Adrress.HardwareErrorStatus.value,
                                self.Adrress.BusWatchdog.value, self.Adrress.Moving.value,
                                self.Adrress.MovingStatus.value, self.Adrress.PresentTemperature.value]
        self.two_byte_values = [self.Adrress.MaxVoltageLimit.value, self.Adrress.MinVoltageLimit.value,
                                self.Adrress.PWMLimit.value, self.Adrress.CurrentLimit.value,
                                self.Adrress.VelocityPGain.value, self.Adrress.VelocityPGain.value,
                                self.Adrress.PositionPGain.value, self.Adrress.PositionIGain.value,
                                self.Adrress.PositionDGain.value, self.Adrress.Feedforward1stGain.value,
                                self.Adrress.Feedforward2ndGain.value, self.Adrress.GoalPWM.value,
                                self.Adrress.GoalCurrent.value, self.Adrress.RealtimeTick.value,
                                self.Adrress.PresentPWM.value, self.Adrress.PresentCurrent.value,
                                self.Adrress.PresentInputVoltage.value]
        self.four_byte_values = [self.Adrress.HomingOffset.value, self.Adrress.MovingThreshold.value,
                                 self.Adrress.AccelerationLimit.value, self.Adrress.VelocityLimit.value,
                                 self.Adrress.MaxPositionLimit.value, self.Adrress.MinPositionLimit.value,
                                 self.Adrress.GoalVelocity.value, self.Adrress.ProfileAcceleration.value,
                                 self.Adrress.ProfileVelocity.value, self.Adrress.GoalPosition.value,
                                 self.Adrress.PresentPosition.value, self.Adrress.PresentVelocity.value,
                                 self.Adrress.VelocityTrajectory.value, self.Adrress.PositionTrajectory.value]

    def init(self, com, baudrate=57600):
        self.portHandler = PortHandler(com)
        baudrates = [9600, 57600, 115200, 1000000, 2000000, 3000000, 4000000]
        try:
            if self.portHandler.openPort():
                self.portHandler.setBaudRate(baudrate)
                self.IDs = [i for i in range(10) if self.packetHandler.read1ByteTxRx(self.portHandler, i, self.Adrress.ID)[1]==0]
                if len(self.IDs) == 0:  # 指定したbaudrateで開かなかったときの処理
                    for br in baudrates:
                        self.portHandler.setBaudRate(br)
                        self.IDs = [i for i in range(10) if self.packetHandler.read1ByteTxRx(self.portHandler, i, self.Adrress.ID)[1] == 0]
                        if len(self.IDs) > 0:
                            break
                return len(self.IDs)
            else:
                return 0
        except Exception:
            return -1


    def exit(self):
        self.write('ALL', self.Adrress.TorqueEnable.value, 0)
        self.portHandler.closePort()


    def reboot(self):
        for i in self.IDs:
            if not self.read(i, self.Adrress.HardwareErrorStatus.value) == 0:
                self.packetHandler.reboot(self.portHandler, i)
                while not self.read(i, self.Adrress.HardwareErrorStatus.value) == 0:
                    pass


    def write(self, axis, INPUT_Adress, value):
        if axis == 'ALL':
            for i in self.IDs:
                if INPUT_Adress in self.one_byte_values:
                    self.packetHandler.write1ByteTxRx(self.portHandler, i, INPUT_Adress, value)
                elif INPUT_Adress in self.two_byte_values:
                    self.packetHandler.write2ByteTxRx(self.portHandler, i, INPUT_Adress, value)
                elif INPUT_Adress in self.four_byte_values:
                    self.packetHandler.write4ByteTxRx(self.portHandler, i, INPUT_Adress, value)
        else:
            if INPUT_Adress in self.one_byte_values:
                self.packetHandler.write1ByteTxRx(self.portHandler, axis, INPUT_Adress, value)
            elif INPUT_Adress in self.two_byte_values:
                self.packetHandler.write2ByteTxRx(self.portHandler, axis, INPUT_Adress, value)
            elif INPUT_Adress in self.four_byte_values:
                self.packetHandler.write4ByteTxRx(self.portHandler, axis, INPUT_Adress, value)


    def read(self, axis, INPUT_Adress):
        ret = 0
        if INPUT_Adress in self.one_byte_values:
            ret, _, _ = self.packetHandler.read1ByteTxRx(self.portHandler, axis, INPUT_Adress)
            if ret >= np.power(2, 7):
                ret = ret - np.power(2, 8)
        elif INPUT_Adress in self.two_byte_values:
            ret, _, _ = self.packetHandler.read2ByteTxRx(self.portHandler, axis, INPUT_Adress)
            if ret >= np.power(2, 15):
                ret = ret - np.power(2, 16)
        elif INPUT_Adress in self.four_byte_values:
            ret, _, _ = self.packetHandler.read4ByteTxRx(self.portHandler, axis, INPUT_Adress)
            if ret >= 2**31:
                ret = ret - 2**32
        return ret


    def Change_OperatingMode(self, axis, INPUT_OPERATING_MODE):
        if axis == 'ALL':
            for i in self.IDs:
                now_frag = self.read(i, self.Adrress.TorqueEnable.value)
                self.write(i, self.Adrress.TorqueEnable.value, 0)
                self.write(i, self.Adrress.OperatingMode.value, INPUT_OPERATING_MODE)
                self.write(i, self.Adrress.TorqueEnable.value, now_frag)
        else:
            now_frag = self.read(axis, self.Adrress.TorqueEnable.value)
            self.write(axis, self.Adrress.TorqueEnable.value, 0)
            self.write(axis, self.Adrress.OperatingMode.value, INPUT_OPERATING_MODE)
            self.write(axis, self.Adrress.TorqueEnable.value, now_frag)
        self.Present_OperatingMode = INPUT_OPERATING_MODE


    def PosCnt_Vbase(self, axis, Goal_position, Goal_velocity):
        self.Change_OperatingMode(axis, self.operating_mode.extended_Position_control.value)
        self.write(axis, self.Adrress.DriveMode.value, 0)
        self.write(axis, self.Adrress.TorqueEnable.value, True)
        self.write(axis, self.Adrress.ProfileVelocity.value, Goal_velocity)
        self.write(axis, self.Adrress.GoalPosition.value, Goal_position)


    def PosCnt_Tbase(self, axis, Goal_position, Goal_Time):
        self.Change_OperatingMode(axis, self.operating_mode.extended_Position_control.value)
        self.write(axis, self.Adrress.DriveMode.value, 4)
        self.write(axis, self.Adrress.TorqueEnable.value, True)
        self.write(axis, self.Adrress.ProfileVelocity.value, Goal_Time)
        self.write(axis, self.Adrress.GoalPosition.value, Goal_position)
