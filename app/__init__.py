from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Initialize Flask app
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import routes after initializing app and db
from app import routes
