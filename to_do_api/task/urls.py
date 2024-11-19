from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from .models import Task
from rest_framework.permissions import IsAuthenticated


# Serializers define the API representation.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['task_name', 'task_created_date', 'users', 'status']
        fields = '__all__'


# ViewSets define the view behavior.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]