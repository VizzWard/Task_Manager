from django.urls import path
from .views import CreateTaskUser, ListTasksActive, GetTaskDetails, UpdateTask, AddCommentView, ViewCommentsTask, UpdateCommentView

urlpatterns = [
    path('create/', CreateTaskUser.as_view(), name='task-list-create'), # Create task
    path('get_tasks/', ListTasksActive.as_view(), name='get-task-list'), # Get all tasks - detail minimal <Only active tasks>
    path('get_tasks/<str:items>', ListTasksActive.as_view(), name='get-task-list'), # Get all tasks - detail minimal <All tasks> (?all=true)
    path('get_task/<int:id>', GetTaskDetails.as_view(), name='get-task-detail'), # Get one task details
    path('update_task/<int:id>', UpdateTask.as_view(), name='update-task'), # Patch and Delete Methods for tasks
    path('comment/<int:id>', AddCommentView.as_view(), name='add-comment'), # Add comment to task
    path('get_comments/<int:id>', ViewCommentsTask.as_view(), name='get-comments'), # Get comments from task
    path('comment/<int:task>/<int:id>', UpdateCommentView.as_view(), name='add-comment'), # Update comment
]