from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from my import db
from my.models import User, Product, Purchase
from my.forms import RegistrationForm, LoginForm

# Создаем Blueprint с именем
main_bp = Blueprint('main', __name__)

# Импортируем вопросы из отдельного файла
from my.data.math_questions import get_all_questions as get_all_math_questions, get_question_by_id as get_math_question_by_id
from my.data.russian_questions import get_all_questions as get_all_russian_questions, get_question_by_id as get_russian_question_by_id
from my.data.history_questions import get_all_history_questions, get_history_question_by_id
from my.data.geography_questions import get_all_questions as get_all_geography_questions, get_question_by_id as get_geography_question_by_id, get_random_questions as get_random_geography_questions
from my.data.biology_questions import get_all_questions as get_all_biology_questions, get_question_by_id as get_biology_question_by_id, get_random_questions as get_random_biology_questions
from my.data.physics_questions import get_all_questions as get_all_physics_questions, get_question_by_id as get_physics_question_by_id, get_random_questions as get_random_physics_questions
from my.data.chemistry_questions import get_all_questions as get_all_chemistry_questions, get_question_by_id as get_chemistry_question_by_id, get_random_questions as get_random_chemistry_questions



# Получаем все вопросы при импорте
math_questions = get_all_math_questions()
russian_questions = get_all_russian_questions()
history_questions = get_all_history_questions()
geography_questions = get_all_geography_questions()
biology_questions = get_all_biology_questions()
physics_questions = get_all_physics_questions()
chemistry_questions = get_all_chemistry_questions()

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

# API для проверки ответов
@main_bp.route('/check_answer', methods=['POST'])
@login_required
def check_answer():
    data = request.get_json()
    question_id = data.get('question_id')
    selected_answer = data.get('answer')
    subject = data.get('subject', 'math')  # Получаем предмет

    # Определяем, из какого модуля брать вопрос
    if subject == 'history':
        question = get_history_question_by_id(question_id)
    elif subject == 'russian':
        question = get_russian_question_by_id(question_id)
    elif subject == 'geography':
        question = get_geography_question_by_id(question_id)
    elif subject == 'biology':
        question = get_biology_question_by_id(question_id)
    elif subject == 'physics':  # Добавляем физику
        question = get_physics_question_by_id(question_id)
    elif subject == 'chemistry':  # Добавьте эту строку
        question = get_chemistry_question_by_id(question_id)
    else:  # по умолчанию математика
        question = get_math_question_by_id(question_id)

    if question:
        is_correct = selected_answer == question['correct_answer']
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
    return render_template('russian.html', subject='Русский язык', questions=russian_questions)

@main_bp.route('/history')
def history():
    history_questions = get_all_history_questions()
    return render_template('history.html', subject='История', questions=history_questions)

@main_bp.route('/geography')
def geography():
    # Получаем случайные вопросы по географии
    geography_questions = get_random_geography_questions(5)
    return render_template('geography.html', subject='География', questions=geography_questions)

@main_bp.route('/biology')
def biology():
    biology_questions = get_random_biology_questions(5)
    return render_template('biology.html', subject='Биология', questions=biology_questions)

@main_bp.route('/physics')
def physics():
    # Получаем случайные вопросы по физике
    physics_questions = get_random_physics_questions(5)
    return render_template('physics.html', subject='Физика', questions=physics_questions)

@main_bp.route('/chemistry')
def chemistry():
    chemistry_questions = get_random_chemistry_questions(5)
    return render_template('chemistry.html', subject='Химия', questions=chemistry_questions)