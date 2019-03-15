
from flask import Flask, render_template, jsonify, request, redirect, url_for
from device import Device
from random import randint

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
app.debug = True
app.run(port='3000', debug=True)