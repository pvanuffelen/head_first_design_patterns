from remote_control_with_undo import RemoteControlWithUndo
from ceiling_fan import CeilingFan

from ceiling_fan_high_command import CeilingFanHighCommand
from ceiling_fan_medium_command import CeilingFanMediumCommand
from ceiling_fan_off_command import CeilingFanOffCommand


class RemoteLoader:
    remote_control = RemoteControlWithUndo()

    ceiling_fan = CeilingFan("Living Room")

    # instance three commands
    ceiling_fan_medium = CeilingFanMediumCommand(ceiling_fan)
    ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

    # Put medium in slot 0 and high in slot 1, also load up the off command
    remote_control.set_command(0, ceiling_fan_medium, ceiling_fan_off)
    remote_control.set_command(1, ceiling_fan_high, ceiling_fan_off)

    remote_control.on_button_was_pushed(0)  # first turn fan on medium
    remote_control.off_button_was_pushed(0)  # then turn it off
    print(remote_control)
    remote_control.undo_button_was_pushed()  # undo! it should go back to medium

    remote_control.on_button_was_pushed(1)  # turn it on to high this time
    print(remote_control)
    remote_control.undo_button_was_pushed()  # and, one more undo; it should go back to medium
