from flask import Flask

from app.config import Config

import os

app = Flask(__name__,
  static_url_path='',
  static_folder='../client')

app.config.from_object(Config)

from app import routes