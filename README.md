# RTRM-Flask
Engineering tools in python with a UI in flask

## Description

A proof of concept for a web interface for python scripts written for engineering purposes. Most of the code is taken from this tutorial:
http://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972

Following frameworks are used on top of Python:
- [Flask](http://flask.pocoo.org/) for the UI framework
- [Bootstrap](http://getbootstrap.com/) to present the UI nicely
  - [Bootsnip](http://bootsnipp.com/forms) to generate the input form
- [jQuery](http://jquery.com/) to post and display form data

A running sample can be found at http://avni.pythonanywhere.com. Please be gentle and don't try to break it.

## Installation
To install it on Ubuntu in a python virtual environment, make sure that you have virtualenv installed and then follow below.

Clone the repository in a folder of your preference.

    git clone https://github.com/avnibu/RTRM-Flask.git

create your virtual environment and activate

    cd RTRM-Flask/
    virtualenv venv
    . venv/bin/activate

Install prerequisites

    pip install -r requirements.txt
