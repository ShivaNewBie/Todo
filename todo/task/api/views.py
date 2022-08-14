from rest_framework import viewsets


from task.api.serializers import TaskSerializer

from task.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    lookup_field = 'slug'

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
   
    def get_queryset(self):
        user = self.request.user 
        return Task.objects.filter(user=user).order_by('-created_at')