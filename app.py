import sqlite3,time
from flask import Flask, render_template, jsonify, request, redirect, url_for
from device import Device
from random import randint
from sensor import updateData

# =========
# Default Values
# 0 - Temperature
# 1 - Moisture
# 2 - PH
# 3 - Humidity
# =========
app = Flask(__name__)
device = Device()

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

@app.route("/saveData",methods = ["POST"])
def saveData():
    if request.method == "POST":
        updateData(time.time(),request.form['temperature'],)





@app.route("/microscope")
def renderMicroscope():
	return render_template("microscope.html")


@app.route("/getSensor")
def returnSensor():
	values = {}
	values['temperatureValue'] = randint(20, 50);
	values['phValue'] = randint(3, 8)
	values['moistureValue'] = randint(40, 80)
	values['humidityValue'] = randint(50, 100)
	return jsonify(values = values)

# =========
# Start App
# =========


if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)