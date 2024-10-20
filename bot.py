from time import sleep
import pyautogui as ai

from database_connector import update_data_status, UCM, actualBalls, actualQrs, actualMarks


def find_image(image, conf=1):
    ai.useImageNotFoundException()
    try:
        ai.locateOnScreen(image, confidence=conf)
        print('"{}" found!'.format(image))
        return True
    except ai.ImageNotFoundException:
        print('"{}" not found!'.format(image))
        return False


def swipe(start_x, start_y, end_x, end_y):
    ai.moveTo(x=start_x, y=start_y)
    ai.mouseDown()
    sleep(1)
    ai.moveTo(end_x, end_y)
    ai.mouseUp()
    sleep(1)


def swipe_banner():
    ai.moveTo(835, 98)
    ai.mouseDown()
    sleep(1)
    ai.moveTo(835, 1090)
    ai.mouseUp()
    sleep(1)


def click(image, conf=0.95, clicks=1, rate=1, delay=1, attempts=-1, pix=0, piy=0):
    print(f"Await {image} — {clicks}!")
    wait = True
    while wait:
        try:
            icon = ai.locateCenterOnScreen(image, confidence = conf)
            print('"{}" found!'.format(image))
            ai.moveTo(icon.x + pix, icon.y + piy)
            ai.click(clicks=clicks, interval=0.1)
            ai.moveTo(5, 5)
            wait = False
            sleep(delay)
            return True
        except ai.ImageNotFoundException:
            print('"{}" not found!'.format(image))
            attempts -= 1
            if attempts == 0:
                wait = False
            sleep(rate)
    return False


def type_text(text):
    ai.write(text, interval=0.1)


def update_data(start, finish, status):
    for i in range(start, finish + 1):
        update_data_status(i, status)


def classic_update(block):
    if block == 0:
        for i in range(0, 51):
            update_data_status(i, UCM.confirmed)
    else:
        for i in range(51, 101):
            update_data_status(i, UCM.confirmed)


def take_screenshot_qr(name_qr):
    ai.screenshot(actualQrs + name_qr + '.png', region=(670, 160, 330, 420))
    print('Скриншот выполнен')
    sleep(0.5)


def take_screenshot_mark(name_qr):
    ai.screenshot(actualMarks + name_qr + '.png', region=(550, 130, 570, 1165))
    print('Скриншот выполнен')
    sleep(0.5)


def take_screenshot_balls(name_qr):
    ai.screenshot(actualBalls + name_qr + '.png', region=(550, 160, 574, 215))
    print('Скриншот выполнен')
    sleep(0.5)


# Переместить окно влево
def window_set_left_pos():
    print("Окно влево")
    ai.keyDown('win')
    ai.keyDown('left')
    sleep(0.15)
    ai.keyUp('win')
    ai.keyUp('left')
    sleep(1.5)
