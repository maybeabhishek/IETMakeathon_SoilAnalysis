
from flask import Flask, render_template, jsonify, request, redirect, url_for
from device import Device
from random import randint
import os
import shutil

app = Flask(__name__)
device = Device()
app.config['UPLOAD_FOLDER'] = "static/uploads/"

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

@app.route("/report")
def renderReport():
	return render_template("report.html")

@app.route("/getSensor")
def returnSensor():
	values = {}
	values['temperatureValue'] = randint(30, 40)
	values['phValue'] = randint(3, 8)
	values['moistureValue'] = randint(40, 80)
	values['humidityValue'] = randint(50, 100)
	return jsonify(values = values)


@app.route("/uploadFile", methods=['POST'])
def uploadFile():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			print("Fail file")
			return "Fail"
		file = request.files['file']
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			print("Fail")
			return "Fail!"
		folder = 'static/uploads/'
		for the_file in os.listdir(folder):
				file_path = os.path.join(folder, the_file)
				try:
						if os.path.isfile(file_path):
								os.unlink(file_path)
						#elif os.path.isdir(file_path): shutil.rmtree(file_path)
				except Exception as e:
						print(e)
		if file:
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'upload.jpg'))
			os.system("python opencv.py")
			return "Success"

# =========
# Start App
# =========


if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)