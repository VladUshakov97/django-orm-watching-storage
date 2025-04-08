# Django ORM Watching Storage

Веб-приложение на Django для просмотра информации о пропусках и посещениях на охраняемом объекте.

## Описание

Приложение отображает:
- Активные пропуска
- Посещения сотрудников
- Время нахождения на территории
- Отметку, является ли визит "долгим"

Проект использует Django ORM для работы с базой данных и загрузку конфигурации через .env файл с помощью библиотеки environs.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/VladUshakov97/django-orm-watching-storage

2. Установка зависимости:

   ```bash
   pip install -r requirements.txt

3. Создайте файл .env и добавьте в него настройки базы данных:

   ```bash
   DB_ENGINE=django.db.backends.postgresql
   DB_HOST=localhost
   DB_PORT=5434
   DB_NAME=your_db_name
   DB_USER=your_username
   DB_PASSWORD=your_password
   
4. Запустите сервер:

   ```bash
   python manage.py runserver

5. Пример запуска кода:

   ```bash
   Performing system checks...

   System check identified no issues (0 silenced).
   April 08, 2025 - 16:03:13
   Django version 3.2, using settings 'project.settings'
   Starting development server at http://0.0.0.0:8000/
   Quit the server with CTRL-BREAK.




