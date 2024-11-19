from rest_framework import serializers
from ..models import Task

class TaskListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'