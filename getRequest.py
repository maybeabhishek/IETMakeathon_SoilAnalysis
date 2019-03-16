import requests

def sendData(temperature,moisture,ph,humidity,device):
    URL = "http://34.73.217.199/saveData"
    params = {"temperature": temperature, "moisture":moisture, "ph":ph, "humidity":humidity, "device":device}
    r = requests.get(url = URL, params= params) 
    data = r.json()
    print(data)
