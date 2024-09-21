# Передача данных и интеграция с интерфейсом
# Блок для передачи данных в интерфейс и на внутреннюю систему управления дроном

def transmit_route_data(route, drone_id, destination):
    # Имитация передачи данных на адрес (пульт оператора)
    print(f"Передача маршрута дрона {drone_id} на {destination}: {route}")
    return True

def save_route_to_drone(route, drone_id):
    # Сохранение данных в памяти дрона
    print(f"Сохранение маршрута дрона {drone_id}: {route}")
    return True
