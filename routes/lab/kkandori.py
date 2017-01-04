from flask import Blueprint, render_template

kkandori = Blueprint('kkandori', __name__)

@kkandori.route('/lab/kkandori')
def welcome():
    return "Hello World"
