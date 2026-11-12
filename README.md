# Swag Labs QA Automation Pet Project

Проект для автоматизации проверки веб-приложения SauceDemo и API-сервиса JSONPlaceholder. В репозитории реализованы UI-тесты на Playwright в стиле Page Object Model и API-тесты на базе `requests`, а также интеграция с `pytest` и `Allure`.

## Что покрыто

### UI-тесты
- авторизация с корректными и некорректными данными;
- добавление товара в корзину;
- проверка количества товаров в корзине;
- переход в корзину и проверка содержимого.

### API-тесты
- `GET /users` — получение списка пользователей;
- `POST /users` — создание нового пользователя.

## Стек
- Python 3
- pytest
- Playwright
- requests
- Allure

## Структура проекта

```text
pet-project-swag-labs/
├── conftest.py              # фикстуры pytest
├── pytest.ini              # настройка pytest и Allure
├── requirements.txt         # зависимости проекта
├── src/
│   └── pages/
│       ├── cart_page.py     # Page Object для корзины
│       ├── inventory_page.py # Page Object для каталога
│       ├── login_page.py    # Page Object для авторизации
│       └── __init__.py
├── tests/
│   ├── test_api.py          # API-тесты
│   ├── test_cart.py         # UI-тесты корзины
│   ├── test_login.py        # UI-тесты авторизации
│   └── __init__.py
├── .gitignore
├── README.md
└── allure-results/          # результаты запуска Allure
```

## Требования
- Python 3.10+
- браузер Chromium для Playwright
- `pip` для установки зависимостей

## Установка

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python -m playwright install chromium
```

## Запуск тестов

Запуск всех тестов:

```bash
pytest
```

Запуск конкретного набора тестов:

```bash
pytest tests/test_login.py
pytest tests/test_cart.py
pytest tests/test_api.py
```

## Генерация отчёта Allure

После запуска тестов отчёты сохраняются в папке `allure-results`.

Чтобы открыть HTML-отчёт локально:

```bash
allure serve allure-results
```

Если Allure CLI не установлен:

```bash
pip install allure-pytest
```

## Примечание

Тесты используют демо-сайт SauceDemo (`https://www.saucedemo.com/`) и JSONPlaceholder API для проверки типовых сценариев автоматизации.
