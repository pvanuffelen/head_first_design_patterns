from command import Command
from no_command import NoCommand


class RemoteControl:

    def __init__(self):
        self.on_commands: list[Command] = []
        self.off_commands: list[Command] = []
        for i in range(7):
            self.on_commands.append(NoCommand())
            self.off_commands.append(NoCommand())

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int):
        self.on_commands[slot].execute()

    def off_button_was_pushed(self, slot: int):
        self.off_commands[slot].execute()

    def __str__(self) -> str:
        my_list = [f"\n------ Remote Control -------\n"]
        for i in range(len(self.on_commands)):
            my_list.append(f"[slot {i}] {self.on_commands[i].__class__.__name__}   {self.off_commands[i].__class__.__name__}\n")
        return "".join(my_list)

