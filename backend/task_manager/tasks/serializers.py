from rest_framework import serializers

from .models import TagsUser, Tasks, Comments

class TagsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsUser
        fields = '__all__'

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'