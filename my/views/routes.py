from flask import Blueprint, render_template, request, jsonify

# Создаем Blueprint
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


# Страница математики с тестом
@main_bp.route('/math')
def math():
    return render_template('math.html', subject='Математика', questions=math_questions)


# API для проверки ответов
@main_bp.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    question_id = data.get('question_id')
    selected_answer = data.get('answer')

    # Находим вопрос
    question = next((q for q in math_questions if q['id'] == question_id), None)

    if question:
        is_correct = selected_answer == question['correct_answer']
        return jsonify({
            'correct': is_correct,
            'correct_answer': question['correct_answer']
        })

    return jsonify({'error': 'Question not found'}), 404


# Остальные страницы предметов (без изменений)
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