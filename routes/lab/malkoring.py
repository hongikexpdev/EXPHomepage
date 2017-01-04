from flask import Blueprint, render_template

malkoring = Blueprint('malkoring', __name__)

@malkoring.route('/lab/malkoring/')
def hell_world():
    return "Hell World"

@malkoring.route('/lab/malkoring/main')
def awesome_main():
    return render_template('lab/malkoring/c.html')
