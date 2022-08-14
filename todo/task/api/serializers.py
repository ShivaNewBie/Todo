from rest_framework import serializers

from task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True)
    created_at = serializers.SerializerMethodField() 
    class Meta:
        model = Task
        fields = ['description','slug','user','status', 'created_at']

    def get_created_at(self,instance): #modified date time
        return instance.created_at.strftime('%B, %d, %Y')