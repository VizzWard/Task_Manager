from django.urls import path
from .views import CreateTaskUser, ListTasksActive, GetTaskDetails, UpdateTask

urlpatterns = [
    path('create/', CreateTaskUser.as_view(), name='task-list-create'), # Create task
    path('get_tasks/', ListTasksActive.as_view(), name='get-task-list'), # Get all tasks - detail minimal <Only active tasks>
    path('get_tasks/<str:items>', ListTasksActive.as_view(), name='get-task-list'), # Get all tasks - detail minimal <All tasks> (?all=true)
    path('get_task/<int:id>', GetTaskDetails.as_view(), name='get-task-detail'), # Get one task details
    path('update_task/<int:id>', UpdateTask.as_view(), name='update-task'), # Patch and Delete Methods
]