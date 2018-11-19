from wpilib.command import CommandGroup
import time

from commands.autotargetangle import AutoTargetAngle
from commands.timedshooter import TimedShooter

class QubeShooter(CommandGroup):
    def __init__(self):
        super().__init__("qube shooter")
        self.addSequential(AutoTargetAngle())
        self.addSequential(TimedShooter(timeout = 2))
