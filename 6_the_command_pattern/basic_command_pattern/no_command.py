from command import Command


class NoCommand(Command):
    """Null  class to avoid having to pass a None type"""
    def execute(self):
        pass

