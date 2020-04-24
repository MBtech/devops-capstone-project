"""This is the main module for the random quotes flask application"""
import logging
from flask import Flask
from flask.logging import create_logger

from numpy.random import choice

APP = Flask(__name__)
LOG = create_logger(APP)
LOG.setLevel(logging.INFO)


@APP.route("/")
def home():
    """ Handler function for the / route """
    html = "<h3>Random Quotes home</h3><br><p>Please send a request \
                to /quote to get a random quote<p>"
    return html.format(format)

@APP.route("/quote", methods=['GET'])
def quote():
    """ Handler function for the /quote route """
    html = "<p>"+ choice(QUOTES) +"<p>"
    return html.format(format)

if __name__ == "__main__":
    F = open('quotes.txt')
    TEXT = F.read()
    QUOTES = TEXT.split("\n\n")
    APP.run(host='0.0.0.0', port=80, debug=True) # specify port=80
