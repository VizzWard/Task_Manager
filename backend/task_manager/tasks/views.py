from datetime import datetime
from django.shortcuts import render
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import generics, permissions, status


from .models import TagsUser, Tasks, Comments
from .serializers import TagsUserSerializer, TasksSerializer, CommentsSerializer

# Create your views here.
class CreateTaskUser(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TasksSerializer

    def post(self, request):
        # Obtener el usuario autenticado
        user = request.user

        # Obtener los datos de la petición
        task_name = request.data.get('task_name') # Requerido

        if not task_name:
            return Response({"error": "El campo 'task_name' es requerido."}, status=status.HTTP_400_BAD_REQUEST)

        task_description = request.data.get('task_description', '') # Opcional
        progress = request.data.get('progress', 0) # Opcional
        priority = request.data.get('priority', False) # Opcional
        start_date = request.data.get('start_date', timezone.now()) # Opcional
        end_date = request.data.get('end_date', None) # Opcional
        tag_name = request.data.get('tag_name', None) # Opcional

        # Crear o obtener el tag si se proporcionó
        try:
            tag = None
            if tag_name:
                tag, created = TagsUser.objects.get_or_create(
                    user=user,
                    name=tag_name
                )
            tarea = Tasks.objects.create(
                user=user,
                name=task_name,
                description=task_description,
                progress=progress,
                priority=priority,
                start_date=start_date,
                end_date=end_date,
                tag=tag if tag else None
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Serializar y devolver la respuesta
        serializer = TasksSerializer(tarea)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListTaskUser(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TasksSerializer

    def get_queryset(self):
        # Obtener el usuario autenticado
        user = self.request.user

        # Obtener las tareas del usuario
        return Tasks.objects.filter(user=user)



