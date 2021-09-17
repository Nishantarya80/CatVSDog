from computerVision import vision
from flask import Flask, render_template, request
import json

app = Flask("Cat Vs Dog")

@app.route("/checking",methods = ['POST'])
def checking():
    f = request.files['imagetocheck']  
    f.save("./computerVision/"+f.filename)
    print(vision.run_example(f.filename))
    return render_template("change.html", result = vision.run_example(f.filename))  


@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
