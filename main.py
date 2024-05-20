import requests
import config

geocode = input('Введите координаты или адрес объекта: ')
# 46.034266 51.533562

geocoder_params = {
    "apikey": config.geocoder_apikey,
    "geocode": geocode,
    "lang": 'ru_RU',
    "format": "json",
    "results": 1}

response = requests.get("http://geocode-maps.yandex.ru/1.x/", params=geocoder_params)
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    toponym_coordinates = toponym["Point"]["pos"]
    toponym_city = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][4]["name"]
    toponym_country = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][0]["name"]

    print(f"\nАдрес: {toponym_address}\n",
          f"Координаты: {toponym_coordinates}\n",
          f"Город: {toponym_city}\n",
          f"Страна: {toponym_country}\n",
          f"Почтовый индекс: {toponym_country}")

    static_params = {
        "apikey": config.static_apikey,
        "ll": ','.join(toponym_coordinates.split()),
        "spn": '0.016457,0.00619'
    }
    res_image = requests.get('https://static-maps.yandex.ru/v1', params=static_params)
    if res_image:
        i = bytes(res_image.content)
        f = open('image.png', 'wb')
        f.write(i)
        f.close()
    else:
        print(f'{res_image.status_code} ({res_image.reason})')
else:
    print(f'{response.status_code} ({response.reason})')
