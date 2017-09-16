from flask import render_template

from andersoldahl import app


@app.route('/')
def home():
    return render_template('home.html')
