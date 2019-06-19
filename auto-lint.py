"""
Automatically generates pylint files for all files in folder.

Use:
    - "python3 auto-lint.py":

"""
import os
import subprocess

if not os.path.exists(os.getcwd() + "/auto-lint"):
    os.mkdir(os.getcwd() + "/auto-lint")

WORKING_DIRECTORY = os.listdir(os.getcwd())
for i in WORKING_DIRECTORY:
    try:
        if i != __file__ and i.split('.')[1] == "py":
            command_string = "pylint " + i.split('.')[0] + \
                              " > " + "auto-lint/" + \
                              i.split('.')[0] + "-$(date +%Y-%m-%d_%H-%M-%S).txt"
            subprocess.call([command_string], shell=True)
    except IndexError:
        pass
