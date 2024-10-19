from datetime import timezone

from rest_framework import serializers
from .models import Task, Comment

#=========================TASK SERIALIZER===============================
class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'due_date', 'created_at', 'updated_at', 'user']

    def validate_due_date(self, value):
        if value and value < timezone.now().date():
            raise serializers.ValidationError("Срок не может быть в прошлом!")
        return value

#===========================COMMENT SERIALIZER===============================
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'task', 'user']
