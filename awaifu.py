#!/usr/bin/env python3

import os
import configparser

configfile = 'config.ini'
config = configparser.ConfigParser()
config.read(configfile)


TURN_ON = ['True', 'true', '1', 'yes', 'Yes', 'YES', 'y', 'Y', 't', 'T', 'on', 'On', 'ON']

debugMode = config['DEFAULT']['debug']
dependencyInstalled = config['DEFAULT']['dependency_installed']


# Check if dependencies are installed
if dependencyInstalled not in TURN_ON and debugMode not in TURN_ON:
    if input('Dependencies not installed. Install now? ') in TURN_ON:
        os.system('pip install -r requirements.txt')
        
        # Update config file
        config['DEFAULT']['dependency_installed'] = 'true'
        with open(configfile, 'w') as configfile:
            config.write(configfile)


# Check for debug mode, then run server
if debugMode in TURN_ON:
    os.environ["FLASK_APP"] = "aWaifu/web"
    os.environ["FLASK_ENV"] = "development"
    os.system("flask run")
else:
    print("Production mode detected. Please set up WSGI.")