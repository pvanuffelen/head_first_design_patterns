from remote_control_with_undo import RemoteControlWithUndo
from light import Light
from tv import TV
from stereo import Stereo
from hottub import Hottub

from light_on_command import LightOnCommand
from light_off_command import LightOffCommand
from tv_on_command import TVOnCommand
from tv_off_command import TVOffCommand
from stereo_on_command import StereoOnCommand
from stereo_off_command import StereoOffCommand
from hottub_on_command import HottubOnCommand
from hottub_off_command import HottubOffCommand

from macro_command import MacroCommand


class RemoteLoader:
    remote_control = RemoteControlWithUndo()

    # create all devices
    light = Light("Living Room")
    tv = TV("Living Room")
    stereo = Stereo("Living Room")
    hottub = Hottub()

    # create on commands
    light_on_command = LightOnCommand(light)
    stereo_on_command = StereoOnCommand(stereo)
    tv_on_command = TVOnCommand(tv)
    hottub_on_command = HottubOnCommand(hottub)

    # create off commands
    light_off_command = LightOffCommand(light)
    stereo_off_command = StereoOffCommand(stereo)
    tv_off_command = TVOffCommand(tv)
    hottub_off_command = HottubOffCommand(hottub)

    # create arrays for on and off commands
    party_on = [light_on_command, stereo_on_command, tv_on_command, hottub_on_command]
    party_off = [light_off_command, stereo_off_command, tv_off_command, hottub_off_command]

    # create macros to hold on and off commands
    party_on_macro = MacroCommand(party_on)
    party_off_macro = MacroCommand(party_off)

    # assign macro command to a button
    remote_control.set_command(0, party_on_macro, party_off_macro)

    # push some buttons to see if works
    print(remote_control)
    print("--- Pushing Macro On ---")
    remote_control.on_button_was_pushed(0)
    print("--- Pushing Macro Off ---")
    remote_control.off_button_was_pushed(0)
