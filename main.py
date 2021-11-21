from flask import Flask, render_template, request
from test import predict

app = Flask(__name__)

@app.route("/")
def home(size=0, qib=0, hni=0, rii=0, price_gain=""):
    return render_template("home.html", size=size, qib=qib, hni=hni, rii=rii, price_gain=price_gain)

@app.route("/predict", methods=['POST'])
def post_predict():
    # size, qib, hni, rii
    size = request.form['size']
    qib = request.form['qib']
    hni = request.form['hni']
    rii = request.form['rii']

    return home(size, qib, hni, rii, predict([size, qib, hni, rii]))


if __name__ == "__main__":
    app.run(debug=False)
