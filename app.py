
from flask import Flask, render_template, json

app = Flask(__name__)


@app.route("/")
def renderRoot():
  return render_template("index.html")




# =========
# Start App
# =========
app.debug = True
app.run(port='3000', debug=True)