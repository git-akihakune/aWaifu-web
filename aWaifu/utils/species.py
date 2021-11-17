import configparser

config = configparser.ConfigParser()
config.read('../config.ini')

RACE_NAMES = config['RACES']['races_name'].split('\n')