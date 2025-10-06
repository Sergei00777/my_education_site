CHEMISTRY_QUESTIONS = [
    {
        'id': 1,
        'question': 'Какой химический элемент обозначается символом "O"?',
        'options': ['Золото', 'Кислород', 'Олово', 'Осмий'],
        'correct_answer': 'Кислород',
        'difficulty': 'easy',
        'category': 'неорганическая химия'
    },
    {
        'id': 2,
        'question': 'Какая кислота содержится в желудочном соке?',
        'options': ['Серная кислота', 'Соляная кислота', 'Азотная кислота', 'Уксусная кислота'],
        'correct_answer': 'Соляная кислота',
        'difficulty': 'easy',
        'category': 'биохимия'
    },
    {
        'id': 3,
        'question': 'Как называется процесс распада вещества под действием электрического тока?',
        'options': ['Диффузия', 'Электролиз', 'Осмос', 'Кристаллизация'],
        'correct_answer': 'Электролиз',
        'difficulty': 'medium',
        'category': 'электрохимия'
    },
    {
        'id': 4,
        'question': 'Какой газ поддерживает горение?',
        'options': ['Азот', 'Углекислый газ', 'Кислород', 'Водород'],
        'correct_answer': 'Кислород',
        'difficulty': 'easy',
        'category': 'неорганическая химия'
    },
    {
        'id': 5,
        'question': 'Какое вещество называют "царской водкой"?',
        'options': ['Смесь серной и азотной кислот', 'Смесь соляной и азотной кислот', 'Чистая азотная кислота', 'Чистая соляная кислота'],
        'correct_answer': 'Смесь соляной и азотной кислот',
        'difficulty': 'medium',
        'category': 'неорганическая химия'
    }
]

# Функции для работы с вопросами
def get_all_questions():
    """Возвращает все вопросы"""
    return CHEMISTRY_QUESTIONS

def get_questions_by_difficulty(difficulty='all'):
    """Возвращает вопросы по уровню сложности"""
    if difficulty == 'all':
        return CHEMISTRY_QUESTIONS
    return [q for q in CHEMISTRY_QUESTIONS if q['difficulty'] == difficulty]

def get_questions_by_category(category='all'):
    """Возвращает вопросы по категории"""
    if category == 'all':
        return CHEMISTRY_QUESTIONS
    return [q for q in CHEMISTRY_QUESTIONS if q['category'] == category]

def get_random_questions(count=5, difficulty='all'):
    """Возвращает случайные вопросы"""
    import random
    if difficulty == 'all':
        questions = CHEMISTRY_QUESTIONS
    else:
        questions = get_questions_by_difficulty(difficulty)

    return random.sample(questions, min(count, len(questions)))

def get_question_by_id(question_id):
    """Находит вопрос по ID"""
    for question in CHEMISTRY_QUESTIONS:
        if question['id'] == question_id:
            return question
    return None