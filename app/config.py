import os
import secrets
import logging

#Configure logging( adjust levels as needed)
logging.basicConfig(filename="app.log",level=logging.DEBUG)

def generate_secret_key():
    return secrets.token_hex(16)

class Config:
    # Secret key generation
    SECRET_KEY = generate_secret_key()

    # MySQL database configuration
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/lead_capture_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
