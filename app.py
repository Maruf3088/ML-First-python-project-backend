from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# Load trained model
with open("placement_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load StandardScaler
with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)


@app.route("/")
def home():
    return "Student Placement Prediction API is running!"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    iq = data["iq"]
    cgpa = data["cgpa"]

    # Create input data
    input_data = np.array([[iq, cgpa]])

    # Scale input using the same scaler used during training
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        result = "Likely to get placement"
    else:
        result = "Likely not to get placement"

    return jsonify({
        "prediction": int(prediction),
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)