from flask import Flask, render_template, request, jsonify
import os
from predict_and_classify import predict_digit
import base64
import re
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    img_data = re.sub('^data:image/.+;base64,', '', data['image'])
    img = Image.open(BytesIO(base64.b64decode(img_data)))
    img.save("input.png")

    digit, parity = predict_digit("input.png")
    return jsonify({"digit": int(digit), "parity": parity})

if __name__ == "__main__":
    app.run(debug=True)
