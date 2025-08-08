from ultralytics import YOLO
import pyautogui
import numpy as np
import cv2
import mss
import time
from pynput.mouse import Controller, Button

###Using the pynput.mouse because pyautogui for some reason doesn't click (everything else is done by pyautogui)
mouse = Controller()

model = YOLO("best.pt")
screen_width, screen_height = pyautogui.size()
sct = mss.mss()
monitor = sct.monitors[1]  # Fullscreen

# Bot settings
CONFIDENCE = 0.4
SHOTS_BEFORE_RELOAD = 8
shot_counter = 0

print("Chicken bot started. Press Ctrl+C to stop.")

while True:

    img = np.array(sct.grab(monitor))
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    results = model.predict(img, conf=CONFIDENCE, verbose=False)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            pyautogui.moveTo(monitor['left'] + cx, monitor['top'] + cy)
            mouse.click(Button.left)
            time.sleep(0.05)
            pyautogui.moveTo(screen_width // 2, screen_height // 2)
            shot_counter += 1
            print(shot_counter)
            

            if shot_counter >= SHOTS_BEFORE_RELOAD:
                mouse.click(Button.right) 
                shot_counter = 0
                time.sleep(0.5)  # Delay to simulate reload (could be smaller?)

    time.sleep(0.01)  # avoid maxing out CPU
