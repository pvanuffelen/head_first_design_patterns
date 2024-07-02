from command import Command


class MacroCommand(Command):  # TODO: implement this code in the remote_loader
    def __init__(self, commands):
        self.commands = commands  # take an array of commands and store them in the macro_command

    def execute(self):
        """When the macro gets executed by the remote, execute those commands one at a time."""
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()
