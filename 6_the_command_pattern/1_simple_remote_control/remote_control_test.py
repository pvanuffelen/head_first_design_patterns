from simple_remote_control import SimpleRemoteControl
from light import Light
from light_on_command import LightOnCommand
from garage_door import GarageDoor
from garage_door_open_command import GarageDoorOpenCommand


class RemoteControlTest:
    remote = SimpleRemoteControl()
    light = Light()
    garage_door = GarageDoor()
    light_on = LightOnCommand(light)
    garage_open = GarageDoorOpenCommand(garage_door)

    remote.set_command(light_on)
    remote.button_was_pressed()
    remote.set_command(garage_open)
    remote.button_was_pressed()
