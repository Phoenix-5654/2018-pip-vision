from wpilib.command import Command


class IntakeToMagazine(Command):

    def __init__(self):
        super().__init__('Intake to Magazine')

        self.requires(self.getRobot().intake_belt)
        self.requires(self.getRobot().magazine_belt)
        self.requires(self.getRobot().shooter_belt)

    def initialize(self):
        self.getRobot().intake_belt.forward()
        self.getRobot().magazine_belt.backward()
        self.getRobot().shooter_belt.backward()

    def end(self):
        self.getRobot().intake_belt.stop()
        self.getRobot().magazine_belt.stop()
        self.getRobot().shooter_belt.stop()
