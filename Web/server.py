# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask.templating import render_template_string

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/fundsearch.html", methods=['GET', 'POST'])
def fundSearch():
    return render_template('fundsearch.html')


@app.route("/predict.html", methods=['GET', 'POST'])
def fundTest():
    return render_template('predict.html')

@app.route("/analysis.html", methods=['GET', 'POST'])
def fundPredict():
    return render_template('analysis.html')


@app.route("/login.html", methods=['GET', 'POST'])
def fundLogin():
    return render_template('login.html')


@app.route("/signup.html", methods=['GET', 'POST'])
def fundSignUp():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
