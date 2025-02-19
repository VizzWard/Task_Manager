# Configuracion api en local

## 1. Instalacion de Virtual Environment

```commandline
python -m venv venv
```

---

## 2. Activar el entorno virtual

```commandline
source venv/bin/activate
```

---

## 3. Instalacion de Dependencies

```commandline
pip install /backend/requeriments.txt
```

---

## Iniciar el proyecto

### 1. Ir a la ruta del proyecto:

```commandline
cd backend\task_manager
```

### 2. Iniciar el proyecto:

```commandline
python manage.py runserver
```

### 3. Crear un superuser

```commandline
python manage.py createsuperuser
```

---