from django.urls import path, include
from rest_framework import routers

from .views import TodoListViewSet

router = routers.DefaultRouter()
router.register(r"todo", TodoListViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
