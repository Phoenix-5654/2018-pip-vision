from wpilib.command import Subsystem


class ConveyorBelt(Subsystem):

    def __init__(self, motor, negate=False):
        super().__init__('Conveyor Belt')

        self.motor = motor

        self.motor.setInverted(negate)

    def forward(self):
        self.motor.set(0.8)

    def backward(self):
        self.motor.set(-0.8)

    def stop(self):
        self.motor.set(0)
