import requests

"""API POINTING TO MANILA"""
url = "https://api.open-meteo.com/v1/forecast?latitude=13.4088&longitude=122.5615&daily=weather_code&models=jma_seamless&current=temperature_2m,is_day,rain,pressure_msl&timezone=Asia%2FSingapore&forecast_days=7"
response = requests.get(url)
location = "Manila"

def getdata(response):
    if response.status_code == 200:
        data  = response.json()
        return data

def printdata(data):
    if not data:
        print("Theres no data to present:")
        return

    current = data.get("current")
    current2 = data.get("current_units")
    temp = current.get("temperature_2m")
    time = current.get("time")
    is_day = current.get("is_day")

    print(f"Location: {location}")
    print(f"Time: {time[11:]}")
    print(f"Date: {time[0:10]}")
    print(f"Temp: {temp} °C")
    print("Day Time" if str(is_day).lower() in ("1","true","yes") else "Nighttime")

    

data = getdata(response)
printdata(data)

