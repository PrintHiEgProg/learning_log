# Learning Log

Журнал обучения на Django. Пользователи создают темы и ведут записи.

## Быстрый запуск

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed          # создаст admin/admin123 + тестовые данные
python manage.py runserver
```

## Деплой (Render / Vercel / Docker)

Задайте одну переменную окружения:

```
DATABASE_URL=postgresql://user:pass@host/dbname?sslmode=require
```

Остальные (`DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS`) — см. `.env.example`.

### Docker

```bash
cp .env.example .env   # вставьте DATABASE_URL
docker compose up -d --build
```

## Аккаунт по умолчанию

Логин: `admin` / Пароль: `admin123`
