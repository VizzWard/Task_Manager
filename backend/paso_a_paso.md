# Task manager api

## Virtual Environment

```commandline
python -m venv venv
source venv/bin/activate
```

---

## Dependencies

**Django, Django REST framework, djangorestframework-simplejwt:**

```commandline
pip install /backend/requeriments.txt
```

---

## Iniciar el proyecto

Ruta del proyecto:

```commandline
cd backend\task_manager
```

Iniciar el proyecto:

```commandline
python manage.py runserver
```

---

## Create Project

```commandline
django-admin startproject task_manager
cd task_manager
```

---

## Make Migrations

```commandline
python manage.py makemigrations
python manage.py migrate
```

---

## Create Superuser

```commandline
python manage.py createsuperuser
```

---

## Create Apps

```commandline
python manage.py startapp accounts_api
python manage.py startapp tasks_api
```

---

## Add Apps to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'accounts_api',
    'tasks_api',
]
```

---

## Add JWT Authentication to `settings.py`

```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```