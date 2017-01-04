from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def hello_world():
    return 'Hello world!'

@main.route('/a')
def example1():
    return render_template('a.html')

@main.route('/a2/<text_input>')
def example1a(text_input):
    return render_template('a2.html', text__input=text_input)

@main.route('/b')
def example2():
    return render_template('b.html')

@main.route('/c')
def example3():
    return render_template('c.html')

@main.route('/roulette')
def roulette():
    return render_template('d.html')
