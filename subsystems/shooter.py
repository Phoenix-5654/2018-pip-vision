from wpilib.command import Subsystem


class Shooter(Subsystem):

    def __init__(self, motor, negate=False):
        super().__init__('Shooter')

        self.motor = motor

        self.motor.setInverted(negate)

    def shoot(self):
        self.motor.set(1)

    def stop(self):
        self.motor.set(0)
