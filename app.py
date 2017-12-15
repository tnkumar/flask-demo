#!/usr/bin/python

from flask import Flask
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
    	name = request.form
    	return render_template('result.html', data=name)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
