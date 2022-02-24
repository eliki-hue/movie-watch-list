from ensurepip import bootstrap
from gettext import install
from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#initializing the application
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# initializing bootstrap
bootstrap = Bootstrap(app)

from app import views
