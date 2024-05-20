import requests

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": 'd632baf7-6d95-49da-a3ba-d967d63ed1f2',
    "geocode": 'Саратов',
    "lang": 'ru_RU',
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    toponym_coordinates = toponym["Point"]["pos"]
    print(toponym_address, "имеет координаты:", toponym_coordinates)
else:
    print(f'{response.status_code} ({response.reason})')