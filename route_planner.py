# Алгоритм маршрута и обработки данных
# Функция, генерирующая полетное задание и проверяющая погодные условия и запретные зоны

import random
from datetime import datetime
import heapq
import math

def create_route(field_coordinates, drone, weather_conditions, no_fly_zones):
    route = []
    for idx, coord in enumerate(field_coordinates):
        point_data = {
            "coordinates": coord,
            "altitude": random.uniform(drone['min_altitude'], drone['max_altitude']),
            "timestamp": datetime.now(),
            "speed": random.uniform(drone['min_speed'], drone['max_speed'])
        }

        # Проверяем погодные условия
        if weather_conditions['wind_speed'] > drone['max_wind_speed']:
            print("Неблагоприятные погодные условия для полета.")
            break

        # Проверяем запретные зоны
        for zone in no_fly_zones:
            if is_in_no_fly_zone(coord, zone):
                print("Точка попадает в запретную зону.")
                break

        route.append(point_data)
    return route

def is_in_no_fly_zone(coord, zone):
    # Простая проверка, находится ли точка внутри запретной зоны
    lat, lon = coord
    zone_lat, zone_lon = zone['coordinates']
    distance = ((lat - zone_lat) ** 2 + (lon - zone_lon) ** 2) ** 0.5
    return distance < zone['radius']


def calculate_routes(field_coords, drone, weather_conditions, algorithms=['dijkstra', 'graph', 'simple']):
    routes = []

    for algorithm in algorithms:
        if algorithm == 'dijkstra':
            route = dijkstra_algorithm(field_coords, drone)
        elif algorithm == 'graph':
            route = graph_algorithm(field_coords, drone)
        elif algorithm == 'hill_climbing':
            route = hill_climbing_algorithm(field_coords, drone)
        else:
            route = simple_algorithm(field_coords, drone)

        routes.append(route)

    return routes


# Рассчитываем евклидово расстояние между двумя точками
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Алгоритм Дейкстры
def dijkstra_algorithm(field_coords, drone):
    start = field_coords[0]
    goal = field_coords[-1]
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {coord: float('inf') for coord in field_coords}
    distances[start] = 0
    previous_nodes = {coord: None for coord in field_coords}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == goal:
            break

        for neighbor in field_coords:
            if neighbor != current_node:
                distance = euclidean_distance(current_node, neighbor)
                new_distance = current_distance + distance

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (new_distance, neighbor))

    # Восстанавливаем путь
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()

    return {"algorithm": "dijkstra", "route": path}


# Алгоритм на основе графов (поиск в глубину)
def graph_algorithm(field_coords, drone):
    start = field_coords[0]
    goal = field_coords[-1]
    stack = [(start, [start])]  # Начальная точка и текущий путь
    visited = set()

    while stack:
        (current_node, path) = stack.pop()

        if current_node in visited:
            continue

        if current_node == goal:
            return {"algorithm": "graph", "route": path}

        visited.add(current_node)

        for neighbor in field_coords:
            if neighbor != current_node and neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return {"algorithm": "graph", "route": []}  # Если путь не найден


# Алгоритм восхождения на холм
def hill_climbing_algorithm(field_coords, drone):
    current_node = field_coords[0]
    goal = field_coords[-1]
    path = [current_node]

    while current_node != goal:
        neighbors = [coord for coord in field_coords if coord != current_node]
        next_node = min(neighbors, key=lambda x: euclidean_distance(x, goal))

        if euclidean_distance(next_node, goal) >= euclidean_distance(current_node, goal):
            break  # Если нет улучшения, заканчиваем
        current_node = next_node
        path.append(current_node)

    return {"algorithm": "hill_climbing", "route": path}


# Простой алгоритм (прямое движение)
def simple_algorithm(field_coords, drone):
    start = field_coords[0]
    goal = field_coords[-1]
    path = [start]
    current_node = start

    while current_node != goal:
        # Находим соседние узлы, исключая текущий
        neighbors = [coord for coord in field_coords if coord != current_node]

        if not neighbors:  # Если нет соседей
            print("Нет доступных соседей для следующего шага.")
            break

        print(f"Текущий узел: {current_node}, Соседи: {neighbors}")

        next_node = min(neighbors, key=lambda x: euclidean_distance(current_node, x))

        if next_node is None:
            print("Не удалось найти следующий узел.")
            break

        path.append(next_node)
        current_node = next_node

    return {"algorithm": "simple", "route": path}

# Выбор лучших маршрутов на основе длины маршрута
def select_best_routes(routes, drone):
    sorted_routes = sorted(routes, key=lambda r: len(r['route']))
    return sorted_routes[:2]