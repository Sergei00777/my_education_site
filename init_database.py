from app import create_app
from my import db

app = create_app()

with app.app_context():
    # Удаляем все таблицы (если нужно пересоздать)
    db.drop_all()

    # Создаем все таблицы
    db.create_all()

    print("База данных успешно создана!")
    print("Созданные таблицы:")
    for table in db.metadata.tables.keys():
        print(f" - {table}")