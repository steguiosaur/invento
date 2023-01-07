from configparser import ConfigParser
from os.path import isfile

def initialize_config():
    if not isfile('config.ini'):
        config_set()

def config_set():
    config = ConfigParser()

    config.read('config.ini')
    config.add_section('settings')
    config.set('settings', 'appearance', 'dark')
    config.set('settings', 'theme', 'blue')
    config.set('settings', 'scale', '100')

    with open('config.ini', 'w') as f:
        config.write(f)

