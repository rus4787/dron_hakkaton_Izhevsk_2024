# Формирование GeoJSON структуры для хранения маршрутов
# Алгоритм, использует сгенерированные данные для построения маршрута и преобразования его в формат GeoJSON

import json


def convert_to_geojson(route, drone_id):
    geojson_data = {
        "type": "FeatureCollection",
        "features": []
    }

    for point in route:
        lat, lon = point['coordinates']
        feature = {
            "type": "Feature",
            "properties": {
                "drone_id": drone_id,
                "altitude": point['altitude'],
                "time": point['timestamp'],
                "speed": point['speed']
            },
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]
            }
        }
        geojson_data["features"].append(feature)

    return json.dumps(geojson_data, indent=2)
