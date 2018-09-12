from wpilib import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.autotargetangle import AutoTargetAngle
from commands.autotargetx import AutoTargetX
from commands.autotargety import AutoTargetY
from commands.operateconveyor import OperateConveyor
from commands.switchmode import SwitchMode


def get_joystick():
    joystick = Joystick(0)

    thumb = JoystickButton(joystick, Joystick.ButtonType.kTop)
    thumb.whenPressed(SwitchMode())

    trigger = JoystickButton(joystick, Joystick.ButtonType.kTrigger)
    trigger.whileHeld(OperateConveyor())

    button_11 = JoystickButton(joystick, 11)
    button_11.whenPressed(AutoTargetY())

    button_12 = JoystickButton(joystick, 12)
    button_12.whenPressed(AutoTargetX())

    button_9 = JoystickButton(joystick, 9)
    button_9.whenPressed(AutoTargetAngle())

    return joystick
