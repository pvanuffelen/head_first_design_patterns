from remote_control import RemoteControl
from light import Light
from garage_door import GarageDoor
from stereo import Stereo

from light_on_command import LightOnCommand
from light_off_command import LightOffCommand
from garage_door_open_command import GarageDoorOpenCommand
from stereo_on_with_cd_command import StereoOnWithCDCommand
from stereo_off_command import StereoOffCommand


class RemoteLoader:
    remote_control = RemoteControl()

    # Create all devices in proper locations
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    garage_door = GarageDoor()
    stereo = Stereo("Living Room")

    # All light command objects
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    # Stereo on and off
    stereo_on_with_cd = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    # Load commands to remote slots
    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, stereo_on_with_cd, stereo_off)

    print(remote_control)  # use the __str__ function to print the slots

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)
    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)
