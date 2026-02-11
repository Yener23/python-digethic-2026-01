from flask import Flask, Response, request
from flask_cors import CORS
import os
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

# Variable umbenannt in 'df_list', um Konflikte zu vermeiden
df_list = pd.read_csv(os.path.join("data", "auto-mpg-test.csv"))

@app.route("/")
def index():
    return {"hello": "world2"}

@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/training_data")
def get_all_training_data():
    # Wir rufen .to_json() auf der Variable 'df_list' auf
    return Response(df_list.to_json(), mimetype="application/json")

@app.route("/predict")
def predict():
    zylinder = float(request.args.get("zylinder"))
    ps = float(request.args.get("ps"))
    gewicht = float(request.args.get("gewicht"))
    beschleunigung = float(request.args.get("beschleunigung"))
    baujahr = float(request.args.get("baujahr"))
    file_to_open = open(os.path.join("data", "models", "baummethoden_lr.pickle"), "rb")
    trained_model = pickle.load(file_to_open)
    file_to_open.close()
    prediction = trained_model.predict(
    [[zylinder, ps, gewicht, beschleunigung, baujahr]]
 )
    print("prediction", prediction[0])
    return {"result": prediction[0]}





