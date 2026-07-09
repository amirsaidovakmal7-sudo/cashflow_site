import gspread
import os
import re
import sys
from google.oauth2.service_account import Credentials
import django
import time
import threading
import datetime

# Поднимаемся вверх: commands -> management -> app -> корень проекта
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )
)

sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

# Импорты после django.setup() — иначе Django не найдёт модули
from config import GOOGLE_KEY
from app.models import Event

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

credentials = Credentials.from_service_account_file(os.path.join(BASE_DIR, 'credentials.json'), scopes=scopes)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

gc = gspread.authorize(credentials)

event = Event.objects.all()


def create_event():
    sheet = gc.open_by_key(GOOGLE_KEY).worksheet('Слоты')
    data = sheet.get_all_values()
    for row in range(1, len(data)):
        print(row)
        id = data[row][0]
        name = data[row][1]
        date = data[row][2]
        orders = data[row][4]
        age_min = data[row][5]
        age_max = data[row][6]
        place_name = data[row][7]
        place_link = data[row][8]
        print(f'Айди: {id} \n'
              f'Название мероприятия: {name} \n'
              f'Дата: {date} \n'
              f'Количество мест: {orders} \n'
              f'Название места: {place_name} \n'
              f'Ссылка: {place_link} \n')

        ev_name = Event.objects.filter(event_name=name)
        ev_date = Event.objects.filter(event_date=date)
        if ev_name and ev_date:
            print('ТАКОЙ ОБЬЕКТ ЕСТЬ')
        else:
            new_event = Event.objects.create(event_name=name, event_date=date, event_place_name=place_name,
                                             event_location=place_link, event_age_min=age_min,
                                             event_age_max=age_max,
                                             event_amount=orders)
            new_event.save()

    return True


def delete_and_change_orders():
    for e in event:
        e.delete()
    print('ОБЬЕКТ УДАЛИЛСЯ')






def do_all_func():
    while True:
        delete_and_change_orders()
        create_event()
        time.sleep(300)


thread = threading.Thread(target=do_all_func)
thread.daemon = True
thread.start()

# Основной поток продолжает свою работу
print("Основной поток продолжает выполняться...")
while True:
    time.sleep(1)
