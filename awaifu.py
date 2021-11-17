#!/usr/bin/env python3

import os
import configparser


config = configparser.ConfigParser()
config.read('config.ini')


TURN_ON = ['True', 'true', '1', 'yes', 'Yes', 'YES', 'y', 'Y', 't', 'T', 'on', 'On', 'ON']


# Check if dependencies are installed
if not config['DEFAULT']['dependency_installed'] in TURN_ON:
    if input('Dependencies not installed. Install now? ') in TURN_ON:
        os.system('pip install -r requirements.txt')


# Check for debug mode, then run server
if config['DEFAULT']['debug'] in TURN_ON:
    os.environ["FLASK_APP"] = "aWaifu/web"
    os.environ["FLASK_ENV"] = "development"
    print("Running in debug mode")
    os.system("flask run")
else:
    print("Production mode detected.")