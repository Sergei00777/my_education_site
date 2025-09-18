import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ваш-секретный-ключ-здесь'
    DEBUG = True
    # Для SQLite базы данных
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False