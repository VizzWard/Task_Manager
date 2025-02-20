import os
import django

# Configurar el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
django.setup()

from users.models import User, UserSettings

for user in User.objects.all():
    if not UserSettings.objects.filter(user=user).exists():
        UserSettings.objects.create(user=user, notification=True, night_mode=False)

print("User settings created successfully.")