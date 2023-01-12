from configparser import ConfigParser
from os.path import isfile

config = ConfigParser()
config.read('config.ini')


# create config at first execute
def initialize_config():
    if not isfile('config.ini'):
        config_set()


# default configuration
def config_set():
    config.add_section('settings')
    config.set('settings', 'appearance', 'Dark')
    config.set('settings', 'theme', 'blue')
    config.set('settings', 'scale', '100')
    config.write(open('config.ini', 'w'))


# appearance [light, dark]
def appearance_save(appearance):
    config.set('settings', 'appearance', appearance)
    config.write(open('config.ini', 'w'))


# color theme [blue, dark-blue, green]
def theme_save(theme):
    config.set('settings', 'theme', theme)
    config.write(open('config.ini', 'w'))


# zoom value [80%, 90%, 100%, 110%, 120%]
def scale_save(scale):
    str_scale = str(int(scale * 100))
    config.set('settings', 'scale', str_scale)
    config.write(open('config.ini', 'w'))

