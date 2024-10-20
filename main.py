import os
import sys

from bot import *
from database_connector import select_data, update_data_counter
from images import *

status = 830, 45, 830, 830


def start_genymotion():
    click(genymotion, clicks=2)
    sleep(3)
    return True


def find_phone(phone):
    load = True
    while load:
        if click(search, attempts=6, conf=0.92):
            type_text(phone)
            load = False
        else:
            click(clear_search, attempts=2)
    return True


def start_phone():
    load = True
    while load:
        click(play)
        click(abort, clicks=0)
        if click(battery_icon, clicks=0, attempts=64):
            load = False
        else:
            click(abort, attempts=4)
    return True


def air_mode_off():
    if click(airplane_icon, attempts=2, clicks=0):
        swipe(status[0], status[1], status[2], status[3])
        click(airplane_on_btn)
        sleep(3)
        click(main_menu)
        sleep(0.5)
    return True


def air_mode_on():
    if not click(airplane_icon, attempts=2, clicks=0):
        swipe(status[0], status[1], status[2], status[3])
        click(airplane_off_btn)
        sleep(2)
        click(main_menu)
        sleep(1)
    return True


def set_mark(phone, id_code):
    marked = False
    click(lukoil_app)
    if click(banner, attempts=12, clicks=0):
        swipe_banner()
    if click(balance, clicks=0, conf=0.87, delay=0.1, rate=0.1, attempts=8):
        take_screenshot_balls(phone)
    click(menu)
    click(history)
    if click(mark_empty, conf=0.98, pix=125, piy=10, attempts=8):
        marked = True
        click(spot_cashier, conf=0.89, attempts=4)
        click(spot_refueller, conf=0.89, attempts=4)
        click(spot_purity, conf=0.89, attempts=4)
    take_screenshot_mark(phone)
    if marked: click(send)
    update_data_status(id_code, UCM.marked)


def get_code(phone, id_code, num_code):
    click(lukoil_app)
    click(lukoil_btn, conf=0.85)
    num_code += 1
    if num_code > 5:
        num_code = 0
    i = 1
    while i < num_code:
        i += 1
        click(qr_update)
    take_screenshot_qr(phone)
    update_data_status(id_code, UCM.updated)
    update_data_counter(id_code, num_code)


def close_app():
    click(main_menu)
    click(tasks)
    swipe(status[2], status[3], status[0], status[1])
    sleep(1)


def stop_phone():
    click(close_phone, conf=0.8)
    click(clear_search, conf=0.92)


def mark_and_update_codes():
    print("Оценка и обновление кодов...")
    get_data = select_data(UCM.confirmed)
    if len(get_data) != 0:
        for el in get_data:
            if steps(el[1], el[0], el[3]):
                print("Оценка и обновление выполнено!" + el[1])
    else:
        print("Кодов для оценки: 0")


def update_codes():
    print("I'm Update Codes...")
    get_data = select_data(UCM.marked)
    if len(get_data) != 0:
        for el in get_data:
            if steps(el[1], el[0], el[3]):
                update_data_status(el[0], UCM.updated)
    else:
        print("Codes to Update: 0")


def steps(phone, id_code, num_code):
    step = 1
    while step != 10:
        match step:
            case 1:
                find_phone(phone)
                step += 1
            case 2:
                start_phone()
                step += 1
            case 3:
                window_set_left_pos()
                step += 1
            case 4:
                air_mode_off()
                step += 1
            case 5:
                set_mark(phone, id_code)
                step += 1
            case 6:
                close_app()
                step += 1
            case 7:
                air_mode_on()
                step += 1
            case 8:
                get_code(phone, id_code, num_code)
                step += 1
            case 9:
                stop_phone()
                step += 1
    return True


def start():
    sleep(1)
    if start_genymotion():
        mark_and_update_codes()
        update_codes()
        sleep(1)
        os.system('shutdown -s')


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    # classic_update(1)
    start()
