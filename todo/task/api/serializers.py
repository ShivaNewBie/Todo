from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Task
        fields = ['description','slug']

    