BIOLOGY_QUESTIONS = [
    {
        'id': 1,
        'question': 'Какая органелла отвечает за производство энергии в клетке?',
        'options': ['Ядро', 'Митохондрия', 'Рибосома', 'Аппарат Гольджи'],
        'correct_answer': 'Митохондрия',
        'difficulty': 'easy',
        'category': 'клеточная биология'
    },
    {
        'id': 2,
        'question': 'Какой процесс обеспечивает растениям возможность создавать органические вещества из неорганических?',
        'options': ['Дыхание', 'Фотосинтез', 'Транспирация', 'Осмос'],
        'correct_answer': 'Фотосинтез',
        'difficulty': 'easy',
        'category': 'ботаника'
    },
    {
        'id': 3,
        'question': 'Какая кровь является универсальным донором?',
        'options': ['I (0)', 'II (A)', 'III (B)', 'IV (AB)'],
        'correct_answer': 'I (0)',
        'difficulty': 'medium',
        'category': 'анатомия и физиология'
    },
    {
        'id': 4,
        'question': 'Какой ученый считается основоположником генетики?',
        'options': ['Чарльз Дарвин', 'Грегор Мендель', 'Луи Пастер', 'Иван Павлов'],
        'correct_answer': 'Грегор Мендель',
        'difficulty': 'easy',
        'category': 'генетика'
    },
    {
        'id': 5,
        'question': 'Какое животное является самым крупным на Земле?',
        'options': ['Африканский слон', 'Синий кит', 'Жираф', 'Белый медведь'],
        'correct_answer': 'Синий кит',
        'difficulty': 'easy',
        'category': 'зоология'
    }
]

# Функции для работы с вопросами
def get_all_questions():
    """Возвращает все вопросы"""
    return BIOLOGY_QUESTIONS

def get_questions_by_difficulty(difficulty='all'):
    """Возвращает вопросы по уровню сложности"""
    if difficulty == 'all':
        return BIOLOGY_QUESTIONS
    return [q for q in BIOLOGY_QUESTIONS if q['difficulty'] == difficulty]

def get_questions_by_category(category='all'):
    """Возвращает вопросы по категории"""
    if category == 'all':
        return BIOLOGY_QUESTIONS
    return [q for q in BIOLOGY_QUESTIONS if q['category'] == category]

def get_random_questions(count=5, difficulty='all'):
    """Возвращает случайные вопросы"""
    import random
    if difficulty == 'all':
        questions = BIOLOGY_QUESTIONS
    else:
        questions = get_questions_by_difficulty(difficulty)

    return random.sample(questions, min(count, len(questions)))

def get_question_by_id(question_id):
    """Находит вопрос по ID"""
    for question in BIOLOGY_QUESTIONS:
        if question['id'] == question_id:
            return question
    return None