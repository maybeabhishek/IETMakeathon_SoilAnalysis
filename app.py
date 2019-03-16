import time
from flask import Flask, render_template, jsonify, request, redirect, url_for
from device import Device
from random import randint
from sensor import *

# =========
# Default Values
# 0 - Temperature
# 1 - Moisture
# 2 - PH
# 3 - Humidity
# =========
app = Flask(__name__)
device = Device()
conn = createConnection()
@app.context_processor
def inject_user():
		return dict(deviceID = device.deviceID)

@app.route("/")
def renderRoot():
	if not device.deviceID:
		return render_template("device.html")
	return render_template("index.html")

@app.route("/setDevice", methods = ["POST"])
def setDevice():
	if request.method == "POST":
		device.setDeviceID(request.form['deviceID'])
		print("Device set as: ", device.deviceID)
		return redirect(url_for("renderRoot"))

# @app.route("/form")
# def rend():
#     return render_template("form.html")

# @app.route("/table")
# def showTable():
#     showAll(conn)
#     return render_template("index.html")

@app.route("/saveData",methods = ["GET"])
def saveData():
    if request.method == "GET":
        updateData(conn,request.form['device'],request.form['temperature'],0)
        updateData(conn,request.form['device'],request.form['moisture'],1)
        updateData(conn,request.form['device'],request.form['ph'],2)
        updateData(conn,request.form['device'],request.form['humidity'],3)
        print("Device value updated in table")
        return "Success"

@app.route("/microscope")
def renderMicroscope():
	return render_template("microscope.html")


@app.route("/getSensor")
def returnSensor():
  values = {}
  values['temperatureValue'] = randint(20, 50)
  values['phValue'] = randint(3, 8)
  values['moistureValue'] = randint(40, 80)
  values['humidityValue'] = randint(50, 100)
  
  return jsonify(values = values)

# =========
# Start App
# =========


if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)