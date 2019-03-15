
from flask import Flask, render_template

app = Flask(__name__)





# =========
# Start App
# =========
app.debug = True
app.run(port='3000', debug=True)