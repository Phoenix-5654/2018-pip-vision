from wpilib.command import Command


class FollowJoystick(Command):

    def __init__(self):
        super().__init__('Follow Joystick')

        self.requires(self.getRobot().drivetrain)

    def execute(self):
        print("Something")
        self.getRobot().drivetrain.drive_robot(
            self.getRobot().joystick.getX(), -self.getRobot().joystick.getY(),
            self.getRobot().joystick.getZ())
