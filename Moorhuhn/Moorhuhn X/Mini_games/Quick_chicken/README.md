To install required dependencies do:

```bash
pip install -r requirements.txt 
```

# Quick Chicken


one of the minigames of Moorhuhn Xtreme, where you have to shoot up as many chickens as you can. There are no time constraints, you have three lives (you loose one if you miss a chicken). This bot doesn't really do things perfectly **BUT** the point of my bots is to get a highscore (and this bot can go as high as infinity). It always looses one health, because the health bar covers a chicken that come out of the chimney.

The bot was made by taking multiple screenshots and training a YOLOv8 model to detect chickens. Then pyautogui was used to control the mouse and click on those chickens (yes it is that simple).
