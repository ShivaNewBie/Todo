from rest_framework import viewsets,generics
from rest_framework.views import APIView


from .serializers import TaskSerializer

from task.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    lookup_field = 'slug'

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
   
    def get_queryset(self):
        user = self.request.user 
        return Task.objects.filter(user=user)