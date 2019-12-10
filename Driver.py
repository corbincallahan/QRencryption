import ReadQR
import Camera
import webbrowser
import Encryptor
from time import sleep

if __name__ == '__main__':
    cam = Camera.camera()
    code = ""
    while not len(code):
        cam.capture("qr")
        code = ReadQR.read("qr.jpg")
        sleep(0.25)

    print("Encrypted: " + code)
    key = int(input("Enter key: "))

    code = code.split(',')
    code[0] = Encryptor.stringToInt(code[0])
    code[1] = Encryptor.stringToInt(code[1])
    decrypted = Encryptor.elGamalDecrypt(code[0], code[1], key)
    decrypted = Encryptor.intToString(decrypted)
    print("Decrypted: " + decrypted)


    webbrowser.open(decrypted)
