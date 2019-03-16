import requests

def sendData(temperature,moisture,ph,humidity):
    URL = "34.73.217.199/saveData"
    params = {"temperature": temperature, "moisture":moisture, "ph":ph, "humidity":humidity}
    r = requests.get(url = URL, params= params) 
    data = r.json()
    print(data)