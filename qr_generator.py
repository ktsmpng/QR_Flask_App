#!/usr/bin/env python

import pyqrcode
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('qr_generator.html', html_img= "..\static\qr.png")

@app.route('/generate', methods=['GET', 'POST'])
def generate():
		
		if request.method == 'POST':
			ssid = request.form['SSID']
			password = request.form['Password']
			info = "WIFI:S:"+str(ssid)+";T:WPA;P:"+str(password)+";;"
			qr = pyqrcode.create(info)
			image = qr.png_as_base64_str(scale=5)
			html_img = '{}'.format(image)
			return render_template('qr_generator.html', html_img = "data:image/png;charset=utf-8;base64," +html_img)

		return render_template('qr_generator.html')

if __name__ == '__main__':
	app.run()