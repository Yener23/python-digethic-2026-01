import requests
import json

longitute = 13.4050
latitude = 52.5200

params = {'daily': 'temperature_2m_max,temperature_2m_min,snowfall_sum', 'latitude': latitude, 'longitude': longitute}

headers = {'Content-Type': 'application/json'}

result = requests.get(
    'https://api.open-meteo.com/v1/forecast',
    params=params,
    headers=headers,
)

if result.status_code == 200:
    data = result.json()
    daily = data.get('daily', {})
    time = daily.get('time', [])
    temperature_2m_max = daily.get('temperature_2m_max', [])
    temperature_2m_min = daily.get('temperature_2m_min', [])
    for i in range(len(time)):
        print(f"Date: {time[i]}, Max Temp: {temperature_2m_max[i]}, Min Temp: {temperature_2m_min[i]}")

else:
    print("Error: {result.status_code}")

#print(result)              # <Response [200]>
#print(result.status_code)  # 200
#print(result.json())
#print(json.dumps(data, indent=2))
