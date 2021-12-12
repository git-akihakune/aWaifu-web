from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import CORS
from utils import waifugen
from utils.security import apiKeyIsValid
from utils.config import domainName, verbose

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
        numberOfProfiles = int(request.form.get('number_of_profiles')) if request.form.get('number_of_profiles') else 4
        multiCultures = request.form.get('multi_cultures') in ['true', 'True']
        bigWaifu = request.form.get('big_waifu') in ['true', 'True']
        faster = request.form.get('faster') in ['true', 'True']
    else:
        apiKey = request.args.get('api_key')
        numberOfProfiles = int(request.args.get('number_of_profiles')) if request.args.get('number_of_profiles') else 4
        multiCultures = request.args.get('multi_cultures') in ['true', 'True']
        bigWaifu = request.args.get('big_waifu') in ['true', 'True']
        faster = request.args.get('faster') in ['true', 'True']

    if not apiKeyIsValid(apiKey):
        return jsonify({
        "status": "error",
        "message": "Invalid API key"
    })

    if verbose: print(f"[!] Processing request from {request.remote_addr}")
    data = waifugen.generate(numberOfProfiles, multiCultures, bigWaifu, faster, verbose)

    return jsonify({
        "status": "success",
        "message": "Here are your waifus",
        "data": data
    })

# A small Easter Egg
@app.route('/admin')
def admin():
    return redirect("https://youtu.be/dQw4w9WgXcQ")