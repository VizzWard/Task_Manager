from django.utils import timezone
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import generics, permissions, status
from django.shortcuts import get_object_or_404


from .models import TagsUser, Tasks, Comments
from .serializers import TagsUserSerializer, TasksSerializer, CommentsSerializer, GetTasksSerializer

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

class GetTaskDetails(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TasksSerializer

    def get(self, request, id=None):
        user = request.user

        task = get_object_or_404(Tasks, id=id, user=user)

        serializer = self.get_serializer(task)
        return Response({"task": serializer.data}, status=status.HTTP_200_OK)

# Vista para obtener las tareas con pocos detalles
class ListTasksActive(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GetTasksSerializer

    def get_queryset(self):
        # Obtener el usuario autenticado
        user = self.request.user

        # Obtener las tareas del usuario
        return Tasks.objects.filter(user=user, state=True)

class UpdateTask(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TasksSerializer

    def patch(self, request, id=None):
        user = request.user

        # 🔍 Buscar la tarea y validar que le pertenece al usuario
        task = get_object_or_404(Tasks, id=id, user=user)

        # Obtener datos opcionales (no obligamos a enviar todos)
        task_name = request.data.get('task_name', task.name)
        task_description = request.data.get('task_description', task.description)
        progress = request.data.get('progress', task.progress)
        priority = request.data.get('priority', task.priority)
        start_date = request.data.get('start_date', task.start_date)
        end_date = request.data.get('end_date', task.end_date)
        tag_name = request.data.get('tag_name', None)  # Opcional

        # 🔄 Actualizar o crear el tag si se proporcionó
        tag = task.tag  # Mantener el tag actual si no se envía uno nuevo
        if tag_name:
            tag, created = TagsUser.objects.get_or_create(user=user, name=tag_name)

        # 📌 Actualizar la tarea existente
        task.name = task_name
        task.description = task_description
        task.progress = progress
        task.priority = priority
        task.start_date = start_date
        task.end_date = end_date
        task.tag = tag
        task.modified_at = timezone.now()

        # Guardar los cambios
        task.save()

        # Serializar y devolver la respuesta
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        user = request.user

        # 🔍 Buscar la tarea y validar que le pertenece al usuario
        task = get_object_or_404(Tasks, id=id, user=user)

        # 🗑️ Eliminar la tarea
        task.delete()

        return Response({"message": "Tarea eliminada correctamente."}, status=status.HTTP_204_NO_CONTENT)



