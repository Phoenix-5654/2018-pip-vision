from wpilib.command import Command

from commands.intaketomagazine import IntakeToMagazine
from commands.intaketoshooter import IntakeToShooter
from commands.magazinetoshooter import MagazineToShooter


class OperateConveyor(Command):
    INTAKE_TO_MAGAZINE = 0
    MAGAZINE_TO_SHOOTER = 1
    INTAKE_TO_SHOOTER = 2

    def __init__(self):

        super().__init__('Operate Conveyor')

        self.command = None

    def initialize(self):

        print('Operate', self.getRobot().conveyor_mode)

        if self.getRobot().conveyor_mode == self.INTAKE_TO_MAGAZINE:

            self.command = IntakeToMagazine()

        elif self.getRobot().conveyor_mode == self.MAGAZINE_TO_SHOOTER:

            self.command = MagazineToShooter()

        else:

            self.command = IntakeToShooter()

        self.command.start()

    def end(self):

        self.command.end()
