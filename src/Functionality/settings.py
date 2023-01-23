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
    config.set('settings', 'tablecolor', 'dark')
    config.set('settings', 'scale', '100')
    config.write(open('config.ini', 'w'))

# appearance [light, dark]
def appearance_save(appearance):
    config.set('settings', 'appearance', appearance)
    config.write(open('config.ini', 'w'))

# display current appearance configuration
def appearance_read():
    appearanceValue = (str(config.get('settings', 'appearance')))
    return appearanceValue

# color theme [blue, dark-blue, green]
def theme_save(theme):
    config.set('settings', 'theme', theme)
    config.write(open('config.ini', 'w'))

# display current theme configuration
def theme_read():
    themeValue = (str(config.get('settings', 'theme')))
    return themeValue

# table theme [light, dark]
def table_theme_save(table):
    config.set('settings', 'tablecolor', table)
    config.write(open('config.ini', 'w'))

# display current theme configuration
def table_theme_read():
    tableThemeValue = (str(config.get('settings', 'tablecolor')))
    return tableThemeValue

# zoom value [80%, 90%, 100%, 110%, 120%]
def scale_save(scale):
    str_scale = str(int(scale * 100))
    config.set('settings', 'scale', str_scale)
    config.write(open('config.ini', 'w'))

# display current scaling configuration
def scale_read():
    scaleValue = (str(config.get('settings', 'scale'))+"%")
    return scaleValue

# return integer value for scaling
def ui_scale_read():
    scaling = int(config.get('settings', 'scale')) /100
    return scaling

