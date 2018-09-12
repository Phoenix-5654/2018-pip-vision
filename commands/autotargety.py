from networktables import NetworkTables
from wpilib.command import PIDCommand


class AutoTargetY(PIDCommand):
    VERTICAL_RES = 360
    NUM_OF_CHECKS = 10

    def __init__(self):

        super().__init__(p=0.18, i=0.4, d=0.6, period=0.1,
                         name='Auto Target Y')

        self.requires(self.getRobot().drivetrain)

        self.getPIDController().setAbsoluteTolerance(10)

        self.getPIDController().setOutputRange(-0.2, 0.2)

        self.setSetpoint(self.VERTICAL_RES // 2)

        self.previous = 0

        self.counter = 0

    def returnPIDInput(self):

        table = NetworkTables.getTable('LiveWindow/Vision')

        self.previous = table.getNumber('y', 0)

        return table.getNumber('y', self.previous)

    def usePIDOutput(self, output):

        if self.previous != 0:
            print(output)
            self.getRobot().drivetrain.drive_robot(x_speed=-output)

    def isFinished(self):

        if self.getPIDController().onTarget():

            self.counter += 1

        else:

            self.counter = 0

        return self.counter == self.NUM_OF_CHECKS
