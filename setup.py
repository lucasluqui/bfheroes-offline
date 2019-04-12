import subprocess
import sys

requirements = open("requirements.txt", "r")

def run():
    for req in requirements.readlines():
        install(req)

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

if __name__ == '__main__':
    run()