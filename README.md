# Автоматизация системы мотивации методом поощрения для детей от 3 лет



```
incentive_motivation/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # Точка входа в приложение
│   ├── config.py             # Конфигурация приложения
│   ├── models/                # Модели SQLAlchemy
│   │   ├── __init__.py
│   │   └── user.py           # Пример модели пользователя
│   │   └── incentive.py       # Пример модели стимула
│   ├── schemas/               # Pydantic схемы для валидации данных
│   │   ├── __init__.py
│   │   └── user.py           # Схемы для пользователя
│   │   └── incentive.py       # Схемы для стимула
│   ├── api/                   # Роуты и контроллеры
│   │   ├── __init__.py
│   │   └── user.py           # Роуты для пользователя
│   │   └── incentive.py       # Роуты для стимула
│   ├── services/              # Логика бизнес-уровня
│   │   ├── __init__.py
│   │   └── user_service.py    # Сервис для работы с пользователями
│   │   └── incentive_service.py# Сервис для работы со стимулами
│   ├── db/                    # Работа с базой данных
│   │   ├── __init__.py
│   │   ├── database.py        # Настройка подключения к БД
│   │   └── migrations/        # Миграции Alembic
│   └── utils/                 # Утилиты и вспомогательные функции
│       ├── __init__.py
│       └── helpers.py         # Вспомогательные функции
│
├── tests/                     # Тесты
│   ├── __init__.py
│   ├── conftest.py            # Конфигурация тестов
│   ├── test_user.py           # Тесты для пользователя
│   └── test_incentive.py      # Тесты для стимулов
│
├── alembic.ini                # Конфигурация Alembic
├── requirements.txt           # Зависимости проекта
└── README.md                  # Документация проекта
```