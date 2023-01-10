from configparser import ConfigParser
from os.path import isfile

config = ConfigParser()
config.read('config.ini')

def initialize_config():
    if not isfile('config.ini'):
        config_set()

def config_set():
    config.add_section('settings')
    config.set('settings', 'appearance', 'Dark')
    config.set('settings', 'theme', 'blue')
    config.set('settings', 'scale', '100')

    config.write(open('config.ini', 'w'))

def appearance_save(appearance):
    config.set('settings', 'appearance', appearance)
    config.write(open('config.ini', 'w'))

def theme_save(theme):
    config.set('settings', 'theme', theme)
    config.write(open('config.ini', 'w'))

def scale_save(scale):
    str_scale = str(int(scale * 100))
    config.set('settings', 'scale', str_scale)
    config.write(open('config.ini', 'w'))
