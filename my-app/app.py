from flask import Flask
from decouple import config

app = Flask(__name__)
application = app
app.secret_key = config('SECRET_KEY')
