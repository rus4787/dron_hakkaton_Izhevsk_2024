# Файл с характеристиками дронов

drones_data = {
    "Geoscan 201": {
        "name": "Geoscan 201",
        "min_speed": 8,
        "max_speed": 40,
        "min_altitude": 100,
        "max_altitude": 4000,
        "max_wind_speed": 10,
        "flight_time": 180
    },
    "XAG M2000 Remote Sensing": {
        "name": "XAG M2000 Remote Sensing",
        "min_speed": 22.22,
        "max_speed": 22.22,
        "min_altitude": 100,
        "max_altitude": 3000,
        "max_wind_speed": 12,
        "flight_time": 90
    },
    "DJI AGRAS T30": {
        "name": "DJI AGRAS T30",
        "min_speed": 7,
        "max_speed": 10,
        "min_altitude": 100,
        "max_altitude": 4500,
        "max_wind_speed": 6,
        "flight_time": 20.5
    },
    "AGROCOPTER A16": {
        "name": "AGROCOPTER A16",
        "min_speed": 3,
        "max_speed": 5,
        "min_altitude": 4,
        "max_altitude": 30,
        "max_wind_speed": 10,
        "flight_time": 11
    }
}

def get_drone(drone_name):
    return drones_data.get(drone_name, None)

def handle_emergency_command(drone, command, field_coords, weather_conditions):
    if command == "вернуться к оператору":
        print(f"{drone['name']} возвращается к оператору.")
        resume_flight(drone, field_coords)
    elif command == "экстренная посадка":
        print(f"{drone['name']} совершает экстренную посадку.")
    else:
        print(f"Команда {command} не распознана.")

def resume_flight(drone, field_coords):
    print(f"{drone['name']} продолжает полет с последней точки.")

def check_weather(drone, weather_conditions):
    return weather_conditions['wind_speed'] <= drone['max_wind_speed']

def start_flight(drone, route):
    print(f"{drone['name']} начинает полет по маршруту: {route}")
