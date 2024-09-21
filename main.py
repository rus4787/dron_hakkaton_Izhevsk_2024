# Сборный скрипт

import drones
import weather_data
import field_data
import geojson_handler
import route_planner
import transmit

def main():
    # Получение данных от оператора
    drone_choice = input("Выберите дрон: ")
    task_type = input("Введите тип задачи (съемка/опрыскивание): ")

    # Получаем характеристики дрона
    drone = drones.get_drone(drone_choice)

    # Загружаем карту и погодные условия
    field_coords = field_data.get_field_coords()
    weather_conditions = weather_data.get_weather()
    no_fly_zones = weather_data.get_no_fly_zones()

    # Проверяем погодные условия
    if not drones.check_weather(drone, weather_conditions):
        print("Погодные условия неподходящие для полета.")
        return

    # Получаем маршруты по разным алгоритмам
    if task_type == "съемка":
        routes = route_planner.calculate_routes(field_coords, drone, weather_conditions, algorithms=['dijkstra', 'graph', 'simple'])
    else:
        routes = route_planner.calculate_routes(field_coords, drone, weather_conditions, algorithms=['complex', 'dijkstra', 'hill_climbing'])

    # Отбор лучших маршрутов
    best_routes = route_planner.select_best_routes(routes, drone)

    # Передача маршрутов на выбор оператору
    print(f"Доступны маршруты: {best_routes}")
    chosen_route = int(input("Выберите маршрут: "))

    # Передача выбранного маршрута на дрон и запуск
    transmit.send_route_to_drone(best_routes[chosen_route])

    # Запуск полета
    drones.start_flight(drone, best_routes[chosen_route])

    # Обработка экстренных команд
    while True:
        command = input("Введите экстренную команду (или 'нет' для продолжения полета): ")
        if command == 'нет':
            continue
        else:
            drones.handle_emergency_command(drone, command, field_coords, weather_conditions)

if __name__ == "__main__":
    main()
