import ReadQR
import Camera
import webbrowser
from time import sleep

if __name__ == '__main__':
    cam = Camera.camera()
    code = ""
    while not len(code):
        cam.capture("qr")
        code = ReadQR.read("qr.jpg")
        sleep(0.25)

    print(code)
    key = input("Enter key: ")

    # decryption stuff

    webbrowser.open(code)
