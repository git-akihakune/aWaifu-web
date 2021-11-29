#!/usr/bin/env python3

import os
import configparser

configfile = 'config.ini'
config = configparser.ConfigParser()
config.read(configfile)

debugMode = config.getboolean('DEFAULT', 'debug')
dependencyInstalled = config.getboolean('DEFAULT', 'dependency_installed')
autoOpenBrowser = config.getboolean('WEB', 'auto_open_browser')
domainName = config['WEB']['domain_name']


def openBrowser():
    import webbrowser
    webbrowser.open(domainName)


if __name__ == '__main__':
    # Check if dependencies are installed
    if not dependencyInstalled and not debugMode:
        if input('Dependencies not installed. Install now? ') in ['y', 'Y', 'yes', 'Yes', 'YES']:
            os.system('pip install -r requirements.txt')
            
            # Update config file
            config['DEFAULT']['dependency_installed'] = 'true'
            with open(configfile, 'w') as configfile:
                config.write(configfile)


    # Check for debug mode, then run server
    if debugMode:
        os.environ["FLASK_APP"] = "aWaifu/web"
        os.environ["FLASK_ENV"] = "development"

        if autoOpenBrowser:
            openBrowser()
        os.system("flask run")
    else:
        print("Production mode detected. Please set up WSGI.")