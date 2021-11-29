from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import CORS
from utils import waifugen
from utils.security import apiKeyIsValid
from utils.config import domainName

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    # To prevent users from accessing the page manually
    if request.referrer != f'{domainName}/settings':
        return redirect("https://youtu.be/dQw4w9WgXcQ")

    if request.method == 'POST':
        data = request.data
        print(data)
        return f"{data}" # redirect(url_for('profile'), code=307)
    return "Invalid request method"



@app.route('/api/profile', methods = ['GET', 'POST'])
def api():
    if request.method == 'POST':
        apiKey = request.form.get('api_key')
    else:
        apiKey = request.args.get('api_key')

    if apiKey == None or not apiKeyIsValid(apiKey):
        return jsonify({
        "status": "error",
        "message": "API key is invalid"
    })

    data = waifugen.generate()

    return jsonify({
        "status": "success",
        "message": "API key is valid",
        "api_key": apiKey,
        "data": data
    })

# A small Easter Egg
@app.route('/admin')
def admin():
    return redirect("https://youtu.be/dQw4w9WgXcQ")