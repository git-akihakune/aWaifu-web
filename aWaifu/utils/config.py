import configparser
import os

configfile = 'config.ini'
ROOT_DIR = os.path.dirname(os.path.abspath(configfile))

config = configparser.ConfigParser()
config.read(os.path.join(ROOT_DIR, configfile))

RACE_NAMES = config['RACES']['races_name'].split('\n')
domainName = config['WEB']['domain_name']
allowedKeys = config['API']['allowed_keys'].split('\n')
verbose = config.getboolean('DEFAULT', 'verbose')