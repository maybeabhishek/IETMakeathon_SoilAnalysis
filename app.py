
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






# =========
# Graph
# =========
@app.route('/graph')
@app.route('/index')
def index(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
	title = {"text": 'My Title'}
	xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	yAxis = {"title": {"text": 'yAxis Label'}}
	return render_template('graph.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)