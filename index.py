from flask import Flask

app = Flask(__name__)

@app.route("/reportof2017")
def reportof2017():
    x = 1+1
    converted_x=str(x)
    return converted_x