import os
from bitbibliotek import app
from flask import render_template, send_from_directory


@app.route('/')
def init():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon')
