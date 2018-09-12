from wpilib.command import Command


class SwitchMode(Command):

    def __init__(self):
        super().__init__('Switch Mode')

    def initialize(self):
        self.getRobot().conveyor_mode = (self.getRobot().conveyor_mode + 1) % 3

        print('Switch', self.getRobot().conveyor_mode)

    def isFinished(self):
        return True
