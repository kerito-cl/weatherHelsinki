import json
import requests
from datetime import datetime

url = "https://api.open-meteo.com/v1/forecast?latitude=60.1695&longitude=24.9354&hourly=temperature_2m&timezone=Europe%2FMoscow&forecast_days=1"
response = requests.get(url)
now = datetime.now()
hora = now.strftime("%H")



df = response.json()


hourlyWeather = df.get("hourly")

weatherList = []

for x, y in hourlyWeather.items():

    weatherList.append(y)

weatherDic = {}

timeList = weatherList[0]

tempList = weatherList[1]

for i in range(len(timeList)):
    weatherDic[timeList[i]] = tempList[i]


    
def tellTemp():

    horaApi = hora

    for x, y in weatherDic.items():
        if x[11:13] == horaApi:
            print(y)
        

tellTemp()
