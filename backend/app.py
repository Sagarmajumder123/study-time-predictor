from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # 👈 THIS LINE FIXES EVERYTHING

model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    input_data = [
        data['hours_studied'],
        data['focus_level'],
        data['sleep_hours'],
        data['difficulty']
    ]

    prediction = model.predict([input_data])[0]

    return jsonify({"predicted_time": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)