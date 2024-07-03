from remote_control_with_undo import RemoteControlWithUndo
from light import Light

from light_on_command import LightOnCommand
from light_off_command import LightOffCommand


class RemoteLoader:
    remote_control = RemoteControlWithUndo()

    living_room_light = Light("Living Room")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    print(remote_control)
    remote_control.undo_button_was_pushed()
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(0)
    print(remote_control)
    remote_control.undo_button_was_pushed()
