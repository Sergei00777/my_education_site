from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Инициализация расширений ДО создания приложения
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Инициализация расширений с приложением
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # Импортируем модели здесь, после инициализации db
    from my import models

    # Создание таблиц
    with app.app_context():
        db.create_all()

    # Регистрируем Blueprint
    from my.views.routes import main_bp
    app.register_blueprint(main_bp)

    return app