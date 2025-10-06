GEOGRAPHY_QUESTIONS = [
    {
        'id': 1,
        'question': 'Какая страна является самой большой по площади в мире?',
        'options': ['Канада', 'США', 'Россия', 'Китай'],
        'correct_answer': 'Россия',
        'difficulty': 'easy',
        'category': 'физическая география'
    },
    {
        'id': 2,
        'question': 'Какая пустыня является самой большой в мире?',
        'options': ['Гоби', 'Сахара', 'Калахари', 'Аравийская пустыня'],
        'correct_answer': 'Сахара',
        'difficulty': 'easy',
        'category': 'физическая география'
    },
    {
        'id': 3,
        'question': 'Какая река является самой длинной в мире?',
        'options': ['Амазонка', 'Нил', 'Янцзы', 'Миссисипи'],
        'correct_answer': 'Нил',
        'difficulty': 'medium',
        'category': 'гидрография'
    },
    {
        'id': 4,
        'question': 'В каком городе находится знаменитый оперный театр "Сиднейский оперный театр"?',
        'options': ['Мельбурн', 'Сидней', 'Канберра', 'Брисбен'],
        'correct_answer': 'Сидней',
        'difficulty': 'easy',
        'category': 'политическая география'
    },
    {
        'id': 5,
        'question': 'Какая гора является самой высокой в мире?',
        'options': ['Килиманджаро', 'Эверест', 'Мак-Кинли', 'Аконкагуа'],
        'correct_answer': 'Эверест',
        'difficulty': 'easy',
        'category': 'физическая география'
    }
]

# Функции для работы с вопросами
def get_all_questions():
    """Возвращает все вопросы"""
    return GEOGRAPHY_QUESTIONS

def get_questions_by_difficulty(difficulty='all'):
    """Возвращает вопросы по уровню сложности"""
    if difficulty == 'all':
        return GEOGRAPHY_QUESTIONS
    return [q for q in GEOGRAPHY_QUESTIONS if q['difficulty'] == difficulty]

def get_questions_by_category(category='all'):
    """Возвращает вопросы по категории"""
    if category == 'all':
        return GEOGRAPHY_QUESTIONS
    return [q for q in GEOGRAPHY_QUESTIONS if q['category'] == category]

def get_random_questions(count=5, difficulty='all'):
    """Возвращает случайные вопросы"""
    import random
    if difficulty == 'all':
        questions = GEOGRAPHY_QUESTIONS
    else:
        questions = get_questions_by_difficulty(difficulty)

    return random.sample(questions, min(count, len(questions)))

def get_question_by_id(question_id):
    """Находит вопрос по ID"""
    for question in GEOGRAPHY_QUESTIONS:
        if question['id'] == question_id:
            return question
    return None