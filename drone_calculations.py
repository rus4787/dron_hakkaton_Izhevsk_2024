# Расчет площади обработки для дронов
# Преобразование характеристик дронов и расчет площади обработки, если таковой нет (например, для AGROCOPTER A16)

def calculate_coverage(drone_specs, task_type):
    if drone_specs['name'] == "AGROCOPTER A16":
        speed = drone_specs['speed_mps']  # м/с
        flight_time = drone_specs['flight_time_sec']  # время полета в секундах
        width = drone_specs['spray_width_m']  # ширина опрыскивания в метрах
        return speed * flight_time * width  # м²
    else:
        return drone_specs['area_coverage_km2'] * 1e6  # км² в м²

# Пример характеристик дрона для расчета
drone_specs_a16 = {
    "name": "AGROCOPTER A16",
    "speed_mps": 3.5,
    "flight_time_sec": 11 * 60,  # 11 минут в секундах
    "spray_width_m": 5
}
print(calculate_coverage(drone_specs_a16, "spraying"))  # Площадь в м²
