from networktables import NetworkTables
from wpilib.command import PIDCommand


class AutoTargetAngle(PIDCommand):
    PARALLEL = -4.5
    HALF_X_RES = 640 // 2
    NUM_OF_CHECKS = 10

    def __init__(self):

        super().__init__(p=0.06, i=0.8, d=0.45, period=0.1,
                         name='Auto Target Angle')

        self.requires(self.getRobot().drivetrain)

        self.getPIDController().setAbsoluteTolerance(5)

        self.getPIDController().setOutputRange(-0.2, 0.2)

        self.setSetpoint(self.PARALLEL)

        self.previous = 0

        self.counter = 0

    def returnPIDInput(self):

        table = NetworkTables.getTable('LiveWindow/Vision')

        self.previous = table.getNumber('angle', 90)

        return table.getNumber('angle', self.previous)

    def usePIDOutput(self, output):

        if self.previous != 90:
            print(output)
            self.getRobot().drivetrain.drive_robot(z_rotation=output)

    def isFinished(self):

        if self.getPIDController().onTarget():

            self.counter += 1

        else:

            self.counter = 0

        return self.counter == self.NUM_OF_CHECKS
