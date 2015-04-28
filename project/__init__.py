from flask import Flask

app = Flask(__name__)
from project import views

def create_app():
	return app