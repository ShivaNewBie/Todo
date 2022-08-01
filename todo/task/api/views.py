from rest_framework import viewsets,generics
from rest_framework.views import APIView


from .serializers import TaskSerializer

from task.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'slug'