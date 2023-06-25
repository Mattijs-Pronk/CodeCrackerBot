import keyboard
import time
import pyautogui

def four_digit_generator():
    for i in range(10000):
        yield str(i).zfill(4)

def handle_macro_key(event):
    if event.name == 'f12':
        generator = four_digit_generator()
        running = True
        for number in generator:
            if not running:
                break

            keyboard.press('e')
            keyboard.release('e')

            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.write(number)
            
            # x = 1197
            # y = 769
            # pyautogui.click(x, y)

            print(number)

            if number == '9999':
                running = False

            # time.sleep(1)

keyboard.on_press(handle_macro_key)

while True:
    if keyboard.is_pressed('esc'):
        break