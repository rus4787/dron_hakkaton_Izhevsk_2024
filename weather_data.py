# Генерация случайных данных (метеостанции и контроль полетов):
# Этот блок создает учебные данные, такие как погодные условия и запретные зоны для полетов

import random
from datetime import datetime, timedelta

def generate_weather_data():
    weather_data = []
    for _ in range(100):  # Генерируем 100 случайных записей
        data_point = {
            "timestamp": datetime.now() - timedelta(hours=random.randint(0, 48)),
            "coordinates": (random.uniform(-90, 90), random.uniform(-180, 180)),
            "humidity": random.uniform(30, 90),
            "wind_speed": random.uniform(0, 20),  # м/с
            "temperature": random.uniform(-30, 50),  # C
            "altitude": random.uniform(0, 5000),  # m
            "interference": random.choice([True, False])  # Состояние радиопомех
        }
        weather_data.append(data_point)
    return weather_data

def generate_no_fly_zones():
    no_fly_zones = []
    for _ in range(20):  # Генерируем 20 запретных зон
        zone = {
            "coordinates": (random.uniform(-90, 90), random.uniform(-180, 180)),
            "radius": random.uniform(1, 10),  # в километрах
            "height_restriction": random.uniform(0, 5000),  # м
            "start_time": datetime.now() - timedelta(hours=random.randint(0, 24)),
            "end_time": datetime.now() + timedelta(hours=random.randint(1, 24)),
        }
        no_fly_zones.append(zone)
    return no_fly_zones

def get_weather():
    # Возвращаем случайные погодные условия
    return {
        "wind_speed": random.uniform(0, 20),
        "temperature": random.uniform(-30, 50),
        "humidity": random.uniform(30, 90)
    }

def get_no_fly_zones(num_zones=5):
    return generate_no_fly_zones()