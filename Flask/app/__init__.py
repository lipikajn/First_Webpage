from flask import Flask
app = Flask(__name__)   #initialising flask object

from app import routes
