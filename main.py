import os
import subprocess


# 현재 스크립트 파일의 디렉토리 경로를 얻기
current_dir = os.path.dirname(__file__)  # 현재 스크립트 파일의 디렉토리 경로


subprocess.run([current_dir+"\\lib\\platform-tools\\adb.exe", "start-server"])
print("현재 디렉토리:", current_dir)

subprocess.run([current_dir+"\\lib\\platform-tools\\adb.exe", "kill-server"])
