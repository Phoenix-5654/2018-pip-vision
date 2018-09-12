import ctre
import wpilib
import wpilib.drive
from commandbased import CommandBasedRobot
from networktables import NetworkTables
from wpilib.command import Command

import oi
from subsystems.conveyorvbelt import ConveyorBelt
from subsystems.drivetrain import Drivetrain
from subsystems.shooter import Shooter


class MyRobot(CommandBasedRobot):

    def robotInit(self):
        Command.getRobot = lambda _: self

        wpilib.CameraServer.launch('vision.py:main')

        NetworkTables.initialize(server='10.56.54.2')

        self.rf_motor = ctre.WPI_VictorSPX(1)
        self.rr_motor = ctre.WPI_VictorSPX(2)

        self.lf_motor = ctre.WPI_VictorSPX(5)
        self.lr_motor = ctre.WPI_VictorSPX(4)

        self.drive = wpilib.drive.MecanumDrive(self.lf_motor,
                                               self.lr_motor,
                                               self.rf_motor,
                                               self.rr_motor)

        self.drivetrain = Drivetrain(self.drive)

        self.shooter_motor = ctre.WPI_VictorSPX(3)

        self.shooter = Shooter(self.shooter_motor)

        self.intake_belt_motor = wpilib.Victor(0)

        self.intake_belt = ConveyorBelt(self.intake_belt_motor)

        self.magazine_belt_motor = wpilib.Victor(1)

        self.magazine_belt = ConveyorBelt(self.magazine_belt_motor,
                                          negate=True)

        self.shooter_belt_motor = wpilib.Victor(2)

        self.shooter_belt = ConveyorBelt(self.shooter_belt_motor,
                                         negate=True)

        self.conveyor_mode = 0

        self.joystick = oi.get_joystick()


if __name__ == '__main__':
    wpilib.run(MyRobot, physics_enabled=True)
