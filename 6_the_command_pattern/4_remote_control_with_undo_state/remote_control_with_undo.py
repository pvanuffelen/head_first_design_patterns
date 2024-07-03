from command import Command
from no_command import NoCommand


class RemoteControlWithUndo:
    def __init__(self):
        self.on_commands: list[Command] = []
        self.off_commands: list[Command] = []
        self.undo_command: Command = NoCommand()
        for i in range(7):
            self.on_commands.append(NoCommand())
            self.off_commands.append(NoCommand())

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_was_pushed(self, slot: int):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_was_pushed(self):
        self.undo_command.undo()

    def __str__(self):
        """
        Function that mimics the toString method of java
        In the example in the book, a StringBuffer is used, which I mimic using a list and the .join() func
        """
        my_list = [f"\n------ Remote Control -------\n"]
        for i in range(len(self.on_commands)):
            my_list.append(f"[slot {i}] {self.on_commands[i].__class__.__name__}   {self.off_commands[i].__class__.__name__}\n")
        my_list.append(f"[undo] {self.undo_command.__class__.__name__}\n")
        return "".join(my_list)
