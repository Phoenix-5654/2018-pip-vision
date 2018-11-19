from wpilib.command import TimedCommand
from commands.magazinetoshooter import MagazineToShooter


class TimedShooter(TimedCommand):
    def __init__(self, timeout = 2):
        super().__init__("Timed shooter", timeout)

    def initialize(self):
        MagazineToShooter().start()

    def end(self):
        MagazineToShooter().end()
