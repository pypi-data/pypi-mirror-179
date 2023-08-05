from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A quick rock paper scissors game'
LONG_DESCRIPTION = 'You can play a rock paper scissors game in any time'

# Setting up
setup(
    name="PyRockPaperScissorsGame",
    version=VERSION,
    author="NeShk",
    author_email="<bodia.nazar4669@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/NeShkApp/RockPaperScissors",
    packages=find_packages(),
    install_requires=['python', 'python3'],
    keywords=['python', 'game', 'function', 'rps', 'rock', 'paper', 'scissors'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)