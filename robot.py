import wpilib
import wpilib.drive
import phoenix5
import rev

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.left_front = phoenix5.WPI_TalonSRX(12)
        self.left_back = phoenix5.WPI_TalonSRX(8)
        self.right_front = rev.CANSparkMax(1, rev.CANSparkLowLevel.MotorType.kBrushless)
        self.right_back = rev.CANSparkMax(4, rev.CANSparkLowLevel.MotorType.kBrushless)
        self.motor_elevacao = phoenix5.WPI_VictorSPX(3)

        
        self.left = wpilib.MotorControllerGroup(self.left_front, self.left_back)
        self.right = wpilib.MotorControllerGroup(self.right_front, self.right_back)
        self.right.setInverted(True)

      
        self.drivetrain = wpilib.drive.DifferentialDrive(self.left, self.right)
        
        self.joystick = wpilib.Joystick(0)


    def teleopPeriodic(self):
        self.drivetrain.arcadeDrive(-self.joystick.getRawAxis(1), self.joystick.getRawAxis(0))

        if self.joystick.getRawButton(1):
            self.motor_elevacao.set(1.0)
        else:
            self.motor_elevacao.set(0.0)
