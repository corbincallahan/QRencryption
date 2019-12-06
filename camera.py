from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (240, 240)

def capture(filename):
    camera.start_preview()
    sleep(1)
    camera.capture(str(filename) + '.jpg')
    camera.stop_preview()