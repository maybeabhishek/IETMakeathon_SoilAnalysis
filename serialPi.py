import serial
from getRequest import sendData
arduino = serial.Serial('/dev/ttyACM0')
while True:
    try:
        data=arduino.readline()
        data = data.decode('utf-8').rstrip()
        data=data.split(',')
        print(data)
        ph = data[0]
        temp = data[1]
        moisture = data[2]
        uv = data[3]
        sendData(temp,moisture,ph,uv,1)
    except Exception as e:
        continue
