PHYSICS_QUESTIONS = [
    {
        'id': 1,
        'question': 'Какая единица измерения используется для измерения силы?',
        'options': ['Джоуль', 'Ватт', 'Ньютон', 'Паскаль'],
        'correct_answer': 'Ньютон',
        'difficulty': 'easy',
        'category': 'механика'
    },
    {
        'id': 2,
        'question': 'Какой закон описывает зависимость между напряжением, силой тока и сопротивлением?',
        'options': ['Закон Ома', 'Закон Ньютона', 'Закон Паскаля', 'Закон Архимеда'],
        'correct_answer': 'Закон Ома',
        'difficulty': 'easy',
        'category': 'электричество'
    },
    {
        'id': 3,
        'question': 'Какое явление объясняет, почему небо голубое?',
        'options': ['Дифракция', 'Интерференция', 'Рассеяние Рэлея', 'Преломление'],
        'correct_answer': 'Рассеяние Рэлея',
        'difficulty': 'medium',
        'category': 'оптика'
    },
    {
        'id': 4,
        'question': 'Как называется устройство для измерения атмосферного давления?',
        'options': ['Термометр', 'Барометр', 'Манометр', 'Гигрометр'],
        'correct_answer': 'Барометр',
        'difficulty': 'easy',
        'category': 'термодинамика'
    },
    {
        'id': 5,
        'question': 'С какой скоростью распространяется свет в вакууме?',
        'options': ['300 000 км/с', '150 000 км/с', '400 000 км/с', '250 000 км/с'],
        'correct_answer': '300 000 км/с',
        'difficulty': 'easy',
        'category': 'оптика'
    }
]

# Функции для работы с вопросами
def get_all_questions():
    """Возвращает все вопросы"""
    return PHYSICS_QUESTIONS

def get_questions_by_difficulty(difficulty='all'):
    """Возвращает вопросы по уровню сложности"""
    if difficulty == 'all':
        return PHYSICS_QUESTIONS
    return [q for q in PHYSICS_QUESTIONS if q['difficulty'] == difficulty]

def get_questions_by_category(category='all'):
    """Возвращает вопросы по категории"""
    if category == 'all':
        return PHYSICS_QUESTIONS
    return [q for q in PHYSICS_QUESTIONS if q['category'] == category]

def get_random_questions(count=5, difficulty='all'):
    """Возвращает случайные вопросы"""
    import random
    if difficulty == 'all':
        questions = PHYSICS_QUESTIONS
    else:
        questions = get_questions_by_difficulty(difficulty)

    return random.sample(questions, min(count, len(questions)))

def get_question_by_id(question_id):
    """Находит вопрос по ID"""
    for question in PHYSICS_QUESTIONS:
        if question['id'] == question_id:
            return question
    return None