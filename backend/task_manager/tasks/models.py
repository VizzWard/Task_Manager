from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.

class TagsUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='unique_tag_per_user')
        ]

    def __str__(self):
        return f'{self.name} | {self.user_id}'

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    progress = models.IntegerField(default=0)
    priority = models.BooleanField(default=False) # False = Low, True = High
    start_date = models.DateTimeField(default=timezone.now, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    tag = models.ForeignKey(TagsUser, on_delete=models.CASCADE, null=True, blank=True)
    state = models.BooleanField(default=True) # True = Active, False = Inactive
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} | {self.state} | {self.end_date} | {self.user_id}'

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_id} | {self.task_id} | {self.comment} | {self.created_at}'