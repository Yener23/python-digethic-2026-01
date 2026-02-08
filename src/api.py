from flask import Flask, Response
from flask_cors import CORS
import os
import pandas as pd

app = Flask(__name__)
CORS(app)

# Variable umbenannt in 'df_list', um Konflikte zu vermeiden
df_list = pd.read_csv(os.path.join("data", "auto-mpg-training.csv"))

@app.route("/", methods=["GET"])
def index():
    return {"hello": "world"}

@app.route("/hello_world", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/training_data", methods=["GET"])
def get_all_training_data():
    # Wir rufen .to_json() auf der Variable 'df_list' auf
    return Response(df_list.to_json(), mimetype="application/json")

