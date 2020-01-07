#!/usr/bin/env python
#coding=utf-8

from flask import Flask,render_template_string

app = Flask(__name__)

@app.route("/")
def index():
        return render_template_string('<h1>Hello Flask</h1>')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
