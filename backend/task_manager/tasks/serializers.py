from rest_framework import serializers

from .models import TagsUser, Tasks, Comments

class TagsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsUser
        fields = '__all__'

class TasksSerializer(serializers.ModelSerializer):
    tag_name = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = [
            'id',
            'name',
            'description',
            'progress',
            'priority',
            'start_date',
            'end_date',
            'state',
            'created_at',
            'modified_at' ,
            'tag_name'
        ]

    def get_tag_name(self, obj):
        return obj.tag.name if obj.tag else None

# Serializador para obtener las tareas con pocos detalles
class GetTasksSerializer(serializers.ModelSerializer):
    tag_name = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = [
            'id',
            'name',
            'progress',
            'priority',
            'tag_name'
        ]

    def get_tag_name(self, obj):
        return obj.tag.name if obj.tag else None

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'