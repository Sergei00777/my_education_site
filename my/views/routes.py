from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from my import db
from my.models import User, Product, Purchase
from my.forms import RegistrationForm, LoginForm

# Создаем Blueprint с именем
main_bp = Blueprint('main', __name__)

# Данные теста по математике
math_questions = [
    {
        'id': 1,
        'question': 'Сколько будет 2 + 2 × 2?',
        'options': ['6', '8', '4', '10'],
        'correct_answer': '6'
    },
    {
        'id': 2,
        'question': 'Чему равен квадратный корень из 64?',
        'options': ['4', '6', '8', '10'],
        'correct_answer': '8'
    },
    {
        'id': 3,
        'question': 'Решите уравнение: 3x - 7 = 14',
        'options': ['x = 5', 'x = 7', 'x = 9', 'x = 11'],
        'correct_answer': 'x = 7'
    },
    {
        'id': 4,
        'question': 'Чему равна площадь круга с радиусом 5? (π ≈ 3.14)',
        'options': ['25π', '50π', '78.5', '31.4'],
        'correct_answer': '78.5'
    },
    {
        'id': 5,
        'question': 'Какое число является простым?',
        'options': ['1', '4', '17', '21'],
        'correct_answer': '17'
    }
]


# Главная страница
@main_bp.route('/')
def index():
    return render_template('index.html')


# Регистрация
@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Регистрация успешна! Теперь вы можете войти.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html', form=form)


# Вход
@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Неверное имя пользователя или пароль', 'danger')

    return render_template('login.html', form=form)


# Выход
@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


# Статистика
@main_bp.route('/stats')
@login_required
def stats():
    return render_template('stats.html', user=current_user)


# Магазин
@main_bp.route('/shop')
@login_required
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)


# Покупка товара
@main_bp.route('/buy/<int:product_id>', methods=['POST'])
@login_required
def buy_product(product_id):
    product = Product.query.get_or_404(product_id)

    if current_user.spend_money(product.price):
        purchase = Purchase(user_id=current_user.id, product_id=product.id)
        db.session.add(purchase)
        db.session.commit()
        flash(f'Вы успешно купили {product.name}!', 'success')
    else:
        flash('Недостаточно денег для покупки', 'danger')

    return redirect(url_for('main.shop'))


# API для проверки ответов (обновленная версия)
@main_bp.route('/check_answer', methods=['POST'])
@login_required
def check_math_answer():  # Изменили имя функции
    data = request.get_json()
    question_id = data.get('question_id')
    selected_answer = data.get('answer')

    question = next((q for q in math_questions if q['id'] == question_id), None)

    if question:
        is_correct = selected_answer == question['correct_answer']

        # Добавляем статистику и деньги
        current_user.add_answer(is_correct)

        return jsonify({
            'correct': is_correct,
            'correct_answer': question['correct_answer'],
            'money': current_user.money
        })

    return jsonify({'error': 'Question not found'}), 404


# Инициализация товаров в магазине
@main_bp.route('/init_products')
def init_products():
    # Удаляем старые товары
    Product.query.delete()

    products = [
        {'name': 'Премиум аватар', 'price': 50, 'category': 'cosmetic',
         'description': 'Стильный аватар для вашего профиля'},
        {'name': 'Золотая рамка', 'price': 100, 'category': 'cosmetic', 'description': 'Эксклюзивная золотая рамка'},
        {'name': 'Специальный значок', 'price': 200, 'category': 'cosmetic',
         'description': 'Уникальный значок достижений'},
        {'name': 'Подсказка на тест', 'price': 30, 'category': 'utility',
         'description': 'Одна подсказка для любого теста'},
        {'name': 'Дополнительная жизнь', 'price': 75, 'category': 'utility',
         'description': 'Возможность перепройти тест'}
    ]

    for product_data in products:
        product = Product(**product_data)
        db.session.add(product)

    db.session.commit()
    return 'Products initialized!'


# Страницы предметов
@main_bp.route('/math')
def math():
    return render_template('math.html', subject='Математика', questions=math_questions)


@main_bp.route('/russian')
def russian():
    return render_template('russian.html', subject='Русский язык')


@main_bp.route('/history')
def history():
    return render_template('history.html', subject='История')


@main_bp.route('/geography')
def geography():
    return render_template('geography.html', subject='География')


@main_bp.route('/biology')
def biology():
    return render_template('biology.html', subject='Биология')


@main_bp.route('/physics')
def physics():
    return render_template('physics.html', subject='Физика')


@main_bp.route('/chemistry')
def chemistry():
    return render_template('chemistry.html', subject='Химия')