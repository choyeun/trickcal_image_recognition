import os
import subprocess
import pytesseract as ts
from PIL import Image
from ppadb.client import Client as AdbClient

deviceport = 53218

# ADB 연결
def adb_connect():
    current_dir = os.path.dirname(__file__)
    subprocess.run([current_dir + "\\lib\\platform-tools\\adb.exe", "start-server"])

    client = AdbClient(host="127.0.0.1", port=5037)
    client.remote_connect("localhost", int(deviceport))
    adbdevice = client.device("localhost:" + str(deviceport))
    if adbdevice is not None:
        print("Adb detected")
    else:
        print("Adb not detected")
        exit(0)
    return adbdevice

# Tesseract-OCR 환경변수 설정
def create_env_var():
    current_dir = os.path.dirname(__file__)
    existing_value = os.environ.get("Path", "")
    additional_value = ";" + current_dir + "\\lib\\Tesseract-OCR\\"
    new_value = existing_value + additional_value
    os.environ["Path"] = new_value

def initialize():
    create_env_var()
    return adb_connect()

if __name__ == "__main__":
    create_env_var()
    adbdevice = adb_connect()
    current_dir = os.path.dirname(__file__)
    x = 500
    y = 300
    cmd = "input touchscreen tap " + str(x) + " " + str(y)
    adbdevice.shell(cmd)
    subprocess.run([current_dir + "\\lib\\platform-tools\\adb.exe", "kill-server"])
    img = Image.open('son.png')
    img2 = Image.open('son2.png')

    text = ts.image_to_string(img, lang='kor')
    text2 = ts.image_to_string(img2, lang='eng')
    print()
    print(text)
    print()
    print(text2)
