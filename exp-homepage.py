from flask import Flask

from routes.main import main

from routes.lab.kkandori import kkandori
from routes.lab.malkoring import malkoring

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(kkandori)
app.register_blueprint(malkoring)

if __name__ == '__main__':
    app.run()
