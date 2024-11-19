from rest_framework.routers import DefaultRouter
from ..viewsets.task_viewsets import taskViewsets

router = DefaultRouter()
auto_api_routers = router


router.register('task', taskViewsets, basename="taskViewsets")
