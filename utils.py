import base64
import requests
import json

# API-KEY
# AIzaSyB8qWYVvfdjkAAYgl-S4yLwCFVsEtWh8ec
url = "https://vision.googleapis.com/v1/images:annotate?key=AIzaSyDUpH8twCqSzx3ymujkdP4jSPs7XqGTLQY"


def encodeImageIntoBase64(imagePath):
    with open(imagePath, "rb") as f:
        return base64.b64encode(f.read())


def detect_Content(encodedImage):
    # img_base64 = base64.b64encode(imagePath)
    headers = {"content-type": "application/json"}

    data = (
        """{
      "requests": [
        {
          "image": {
                   "content": '"""
        + encodedImage[:-1]
        + """'

                    },

          "features": [
            {
              "type": "TEXT_DETECTION"
            }
          ]
        }
      ]
    }"""
    )
    r = requests.post(url, headers=headers, data=data)
    result = json.loads(r.text)
    return result





