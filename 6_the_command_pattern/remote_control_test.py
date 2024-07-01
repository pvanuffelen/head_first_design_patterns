from simple_remote_control import SimpleRemoteControl
from light import Light
from light_on_command import LightOnCommand

class RemoteControlTest():

    remote = SimpleRemoteControl()
    light = Light()
    light_on = LightOnCommand(light)

    remote.set_command(light_on)
    remote.button_was_pressed()