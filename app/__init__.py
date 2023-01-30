from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f54d04e74a1804581df52430de94eb165a161c1154917b90'

from app import routes