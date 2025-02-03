import pyautogui
import time

print("将鼠标移动到目标位置，按下 Ctrl+C 结束。")
try:
    while True:
        x, y = pyautogui.position()
        print(f"鼠标位置: ({x}, {y})", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n结束坐标检测。")