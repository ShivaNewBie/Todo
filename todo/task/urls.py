from django.urls import path,include

from rest_framework.routers import DefaultRouter

from task.api import views as tv 

router = DefaultRouter()
router.register(r'tasks', tv.TaskViewSet)

urlpatterns = [
    path('', include(router.urls))
]