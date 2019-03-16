import requests
import os
os.system("rm micro.jpg")
os.system("fswebcam --no-banner micro.jpg")
url = 'http://192.168.43.156:8080/uploadFile'
files = {'file': open('micro.jpg', 'rb')}
requests.post(url, files=files)