from classifier import get_prediction
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/predict_number", methods = ["POST"])
def pred_data():
    image = request.files.get("digit")
    predictions = get_prediction(image)
    return(jsonify({
        "prediction":prediction
    }))
if __name__ == "__main__":
    app.run()