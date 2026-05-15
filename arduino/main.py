" тут микро пайтон. Тут уже ты работаешь) "

import time
import network
import urequests

# Настройки Wi-Fi
WIFI_SSID = "ИМЯ_ВАШЕГО_WI-FI"
WIFI_PASS = "ПАРОЛЬ_ОТ_WI-FI"

# URL вашего эндпоинта (замените IP на адрес вашего компьютера)
API_URL = "http://192.168.1" 

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(WIFI_SSID, WIFI_PASS)
        for _ in range(10):
            if wlan.isconnected(): break
            time.sleep(1)
    return wlan.isconnected()

if connect_wifi():
    try:
        print("Отправка триггера на сервер...")

        response = urequests.get(API_URL)
        
        # Проверяем код ответа (200 означает, что всё прошло успешно)
        if response.status_code == 200:
            print("Статус: ОК")
        else:
            print("Сервер ответил с ошибкой. Код:", response.status_code)
            
        # Освобождаем память платы
        response.close()
        
    except Exception as e:
        print("Не удалось связаться с сервером:", e)
