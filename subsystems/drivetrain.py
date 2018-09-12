from wpilib.command import Subsystem

from commands.followjoystick import FollowJoystick


class Drivetrain(Subsystem):

    def __init__(self, drive):
        super().__init__('Drivetrain')

        self.drive = drive

    def drive_robot(self, y_speed=0, x_speed=0, z_rotation=0):
        self.drive.driveCartesian(y_speed, x_speed, z_rotation)

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())
