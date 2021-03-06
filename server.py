from computerVision import vision
from flask import Flask, render_template, request
from flask import jsonify
import json
import base64
from PIL import Image
import io

app = Flask(__name__)

# New route
@app.route("/checking2",methods = ['POST'])
def checking2():
    f = request.json
    file = f["file"]
    print(f["name"])
    out = base64.b64decode(file)
    image = Image.open(io.BytesIO(out))
    image = image.resize((224,224))
    output = int(vision.run_example2(image))

    if(output == 1):
        result = "Dog"
    else:
        result = "Cat"

    return jsonify({"Output":result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
