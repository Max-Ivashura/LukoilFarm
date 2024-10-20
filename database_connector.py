import sqlite3


class UCM:
    updated = 1
    confirmed = 2
    marked = 3


con_str = 'LukoilCodes.sql'
actualQrs = 'E:\\LukoilQRs\\ActualQRs\\'
actualMarks = 'E:\\LukoilQRs\\ActualMarks\\'
actualBalls = 'E:\\LukoilQRs\\ActualBalls\\'


# Для информации, каким кодам обновлять статус
def select_data(status):
    try:
        conn = sqlite3.connect(con_str)
        curs = conn.cursor()
        curs.execute("SELECT * FROM codes WHERE ucm = '%s'" % status)
        result = curs.fetchall()
        conn.close()

        if result is None:
            print("Нет данных")
        else:
            print(f"Данных загружено: {len(result)}")
            return result
    except Exception as error:
        print(error)
        print(f"---При загрузке данных:  '{status}' кодов произошла ошибка!")


# Для обновления кодам статуса
def update_data_status(id_code, status):
    try:
        conn = sqlite3.connect(con_str)
        curs = conn.cursor()
        curs.execute(f"UPDATE codes SET ucm = {status} WHERE id = {id_code}")
        conn.commit()
        conn.close()
        print(f"Статус изменён на: '{status}' для: {id_code} ")
    except Exception as error:
        print(error)
        print(f"---При обновлении статуса({status}) кода для ({id_code}) произошла ошибка!")


# Для обновления кодам счетчика
def update_data_counter(id_code, num):
    try:
        conn = sqlite3.connect(con_str)
        curs = conn.cursor()
        curs.execute(f"UPDATE codes SET numCode= {num} WHERE id = {id_code}")
        conn.commit()
        conn.close()
        print(f"numCode изменён на: '{num}' для: {id_code} ")
    except Exception as error:
        print(error)
        print(f"---При обновлении numCode({num}) кода для ({id_code}) произошла ошибка!")
