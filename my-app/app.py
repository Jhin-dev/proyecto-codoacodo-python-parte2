from flask import Flask
from decouple import config

def create_app():
  app = Flask(__name__)
  application = app
  app.secret_key = config('SECRET_KEY')
