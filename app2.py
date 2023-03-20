from flask import Flask, request, Response, url_for, render_template
from flask_cors import CORS
import json
from utils import detect_Content, encodeImageIntoBase64
import base64
import os

app = Flask(__name__)
os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")
CORS(app)

inputFileName = "Example_01.png"
imagePath = "images/" + inputFileName


@app.route("/")
def index():
    encodedImageStr = encodeImageIntoBase64(imagePath=imagePath)
    ig = str(encodedImageStr)
    ik = ig.replace("b'", "")
    numberPlateVal = detect_Content(ik)
    return render_template("index.html", prediction=numberPlateVal)


if __name__ == "__main__":
    app.run(debug=True)
