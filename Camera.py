from picamera import PiCamera
from time import sleep


class camera:
    def __init__(self):
        self.cam = PiCamera()
        self.cam.resolution = (240, 240)
        self.cam.start_preview()
        sleep(1)

    def capture(self, filename):
        self.cam.capture(str(filename) + '.jpg')

    def __del__(self):
        self.cam.stop_preview()
