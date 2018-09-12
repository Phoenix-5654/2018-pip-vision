from wpilib.command import Command


class IntakeToShooter(Command):

    def __init__(self):
        super().__init__('Intake to Shooter')

        self.requires(self.getRobot().intake_belt)
        self.requires(self.getRobot().magazine_belt)
        self.requires(self.getRobot().shooter_belt)
        self.requires(self.getRobot().shooter)

    def initialize(self):
        self.getRobot().intake_belt.forward()
        self.getRobot().magazine_belt.backward()
        self.getRobot().shooter_belt.backward()
        self.getRobot().shooter.shoot()

    def end(self):
        self.getRobot().intake_belt.stop()
        self.getRobot().magazine_belt.stop()
        self.getRobot().shooter_belt.stop()
        self.getRobot().shooter.stop()
