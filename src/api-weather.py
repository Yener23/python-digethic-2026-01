import requests
import json

# Koordinaten für Berlin
longitude = 13.4050
latitude = 52.5200

# Parameter für das historische Archiv
params = {
    'latitude': latitude,
    'longitude': longitude,
    'start_date': '2019-03-08',
    'end_date': '2019-03-08',
    'daily': 'temperature_2m_max,temperature_2m_min,rain_sum',
    'timezone': 'Europe/Berlin'
}

# Wichtig: Der Endpunkt für historische Daten ist 'archive'
url = 'https://archive-api.open-meteo.com/v1/archive'

result = requests.get(url, params=params)

if result.status_code == 200:
    data = result.json()
    daily = data.get('daily', {})

    # Da wir nur einen Tag abgefragt haben, nehmen wir jeweils den ersten Index [0]
    date = daily.get('time', [None])[0]
    t_max = daily.get('temperature_2m_max', [None])[0]
    t_min = daily.get('temperature_2m_min', [None])[0]
    rain = daily.get('rain_sum', [0])[0]

    print(f"Wetterbericht für den {date}:")
    print(f"Max. Temperatur: {t_max}°C")
    print(f"Min. Temperatur: {t_min}°C")
    print(f"Regenmenge: {rain} mm")
else:
    print(f"Fehler bei der Abfrage: {result.status_code}")

#print(result)              # <Response [200]>
#print(result.status_code)  # 200
#print(result.json())
#print(json.dumps(data, indent=2))
