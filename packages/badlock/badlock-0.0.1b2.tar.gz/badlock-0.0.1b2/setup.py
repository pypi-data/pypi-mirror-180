from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1b2'
DESCRIPTION = "Badlock"
LONG_DESCRIPTION = 'This package will simply fuck with your pc...'

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
    install_requires=["keyboard"],
    keywords=['mouse lock', 'hack', 'break pc', 'destroy pc', 'troll'],
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
print("here")