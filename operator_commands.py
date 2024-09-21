# Обработка команд от оператора
# Блок обработки типовых команд оператора (возвращение на базу или экстренная посадка)

def handle_operator_command(command, drone_position):
    base_position = (0, 0)  # Позиция базы, замените на реальные координаты

    if command == "return_to_base":
        # Логика возврата на место взлета
        print("Drone is returning to base...")
        return "Drone is returning to base", base_position

    elif command == "emergency_landing":
        # Логика экстренной посадки
        print("Drone is performing emergency landing...")

        # Безопасное место для посадки — последняя точка поворота
        landing_position = drone_position  # Позиция, где дрон остановился
        print(f"Landing at position: {landing_position}")
        return "Drone is performing emergency landing", landing_position

    elif command == "hold_position":
        # Логика приостановки
        print("Drone is holding position...")
        # Дрон зависает в текущей позиции
        # Сохраняем текущую позицию и сообщаем оператору
        print(f"Drone is hovering at position: {drone_position}")
        return "Drone is holding position", drone_position

    else:
        return "Unknown command", drone_position
