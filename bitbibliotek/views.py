import os
from bitbibliotek import app
from flask import render_template, send_from_directory, redirect, request


@app.route('/')
@app.route('/<val>')
def index(val=None):
    res = val == str(app.config['SECRET'])
    return render_template('index.html', authed=res)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == app.config['USERNAME'] and request.form['password'] == app.config['PASSWORD']:
            return redirect(f'/{app.config["SECRET"]}')
    return render_template('login.html')
