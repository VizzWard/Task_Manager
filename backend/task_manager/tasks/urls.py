from django.urls import path
from .views import CreateTaskUser, ListTaskUser

urlpatterns = [
    path('create/', CreateTaskUser.as_view(), name='task-list-create'),
    path('get_tasks/', ListTaskUser.as_view(), name='get-task-list'),
]