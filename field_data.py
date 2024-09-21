# Генерация случайных координат для поля
# Функция для генерации координат участка работы, которые позже будут использоваться для создания маршрутов

import random

def generate_field_coordinates(num_points=5):
    field_coordinates = []
    for _ in range(num_points):
        lat = random.uniform(-90, 90)
        lon = random.uniform(-180, 180)
        field_coordinates.append((lat, lon))
    return field_coordinates

def get_field_coords(num_points=5):
    return generate_field_coordinates(num_points)

import random

def generate_field_coordinates(num_points=5):
    field_coordinates = []
    for _ in range(num_points):
        lat = random.uniform(-90, 90)
        lon = random.uniform(-180, 180)
        field_coordinates.append((lat, lon))
    return field_coordinates

def get_field_coords(num_points=5):
    return generate_field_coordinates(num_points)