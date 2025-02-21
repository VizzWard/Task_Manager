from django.urls import path
from .views import CreateTaskUser, ListTasksActive, GetTaskDetails, UpdateTask

urlpatterns = [
    path('create/', CreateTaskUser.as_view(), name='task-list-create'),
    path('get_tasks/', ListTasksActive.as_view(), name='get-task-list'),
    path('get_task/<int:id>', GetTaskDetails.as_view(), name='get-task-detail'),
    path('update_task/<int:id>', UpdateTask.as_view(), name='update-task'), # Patch and Delete Methods
]