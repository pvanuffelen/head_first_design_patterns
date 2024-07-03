from command import Command
from stereo import Stereo


class StereoOffCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()
