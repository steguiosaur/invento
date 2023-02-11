from os.path import isfile
import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

def dependency_installer():
    # executes installer on first startup
    if not isfile('./config.ini'):
        with open("requirements.txt") as f:
            dependencies = f.read().splitlines()

        for package in dependencies:
            try:
                __import__(package)
            except ImportError:
                install(package)
