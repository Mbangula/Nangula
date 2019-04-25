# Nangula Chatbot

## Requirements
* Python 3.6
* [Python virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


## Installation
checkout git repository:

    git clone ...
    cd Nangula

Choose to install requirements either with pip or conda

### Create virtual environment with pip

    virtualenv --python=<path-to-python-3.6> env

activate virtual environment

    source env/bin/activate

install requirements

    pip install -r requirements.txt

Prepare nltk

    >>> import nltk
    >>> nltk.download('punkt')

You may need to install Pytorch [manually](http://pytorch.org/)

### Create virtual environment with conda

    conda create -n env python=3.6
    source activate env

Install requirements using

    conda install <package-name>

For prompt_toolkit 2.0 use

    conda install pip
    pip install -e git+https://github.com/jonathanslenders/python-prompt-toolkit@2.0#egg=prompt_toolkit

Prepare nltk

    >>> import nltk
    >>> nltk.download('punkt')

You may need to install Pytorch [manually](http://pytorch.org/)

### Install chromedriver

With Linux

    sudo apt-get install chromium-chromedriver

With Mac, using [Hombrew](https://brew.sh/)

    brew install chromedriver

## Running the app

    python app.py

## Virtualenv
When you are done, deactivate virtual environment

    deactivate

## Chat commands
    debug
    stop debug
    please translate
    Translate
    please search
    Search 
    stop searching
    stop translating
    bye
    goodbye
    exit
