from os.path import isfile
import os

package = [
    "customtkinter",
    "pillow"
]

# import or install required dependencies
def dependency_install():    
    if not isfile('./account.db'):
        for x in range(0, len(package)):
            try:
                __import__(package[x])
            except ImportError:
                os.system("pip install " + package[x])
