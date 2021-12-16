import configparser
import os

configfile = 'config.ini'
ROOT_DIR = os.path.dirname(os.path.abspath(configfile))

config = configparser.ConfigParser()
config.read(os.path.join(ROOT_DIR, configfile))

verbose = config.getboolean('DEFAULT', 'verbose')
allowedKeys = config['API']['allowed_keys'].split('\n')