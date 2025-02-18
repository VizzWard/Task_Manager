# Task manager api

## Dependencies

**Django y Django REST framework:**

```commandline
pip install django
pip install djangorestframework
```

## Virtual Environment

```commandline
python -m venv venv
source venv/bin/activate
```

## Create Project

```commandline
django-admin startproject task_manager
cd task_manager
```

## Create Apps

```commandline
python manage.py startapp accounts_api
python manage.py startapp tasks_api
```