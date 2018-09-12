from networktables import NetworkTables
from wpilib.command import PIDCommand


class AutoTargetX(PIDCommand):
    HORIZONTAL_RES = 640
    NUM_OF_CHECKS = 10

    def __init__(self):

        super().__init__(p=0.18, i=0.4, d=0.6, period=0.1,
                         name='Auto Target X')

        self.requires(self.getRobot().drivetrain)

        self.getPIDController().setAbsoluteTolerance(10)

        self.getPIDController().setOutputRange(-0.3, 0.3)

        self.setSetpoint(self.HORIZONTAL_RES // 2)

        self.previous = 0

        self.counter = 0

    def returnPIDInput(self):

        table = NetworkTables.getTable('LiveWindow/Vision')

        self.previous = table.getNumber('x', 0)

        return table.getNumber('x', self.previous)

    def usePIDOutput(self, output):

        if self.previous != 0:
            print(output)
            self.getRobot().drivetrain.drive_robot(y_speed=-output)

    def isFinished(self):

        if self.getPIDController().onTarget():

            self.counter += 1

        else:

            self.counter = 0

        return self.counter == self.NUM_OF_CHECKS
