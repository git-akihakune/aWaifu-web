from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os
from utils import security

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/profile')
def profile():
    # To prevent user from manually getting to the site
    if os.environ["FLASK_ENV"] == "production" and security.checkPreviousSite(request.referrer):
        return redirect(url_for('index'))
    return render_template('profile.html')


# A small Easter Egg
@app.route('/admin')
def admin():
    return redirect("https://youtu.be/dQw4w9WgXcQ")