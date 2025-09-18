from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from my import db  # Это должно работать теперь
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    money = db.Column(db.Integer, default=0)
    total_answers = db.Column(db.Integer, default=0)
    correct_answers = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Связь с покупками
    purchases = db.relationship('Purchase', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def add_money(self, amount):
        self.money += amount
        db.session.commit()

    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
            db.session.commit()
            return True
        return False

    def add_answer(self, is_correct):
        self.total_answers += 1
        if is_correct:
            self.correct_answers += 1
            self.money += 1
        db.session.commit()

    def get_accuracy(self):
        if self.total_answers == 0:
            return 0
        return (self.correct_answers / self.total_answers) * 100


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200))
    category = db.Column(db.String(50))


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)
    quantity = db.Column(db.Integer, default=1)


# Двигаем user_loader в конец файла
def load_user(user_id):
    from my import login_manager
    return User.query.get(int(user_id))


# Устанавливаем user_loader
from my import login_manager

login_manager.user_loader(load_user)