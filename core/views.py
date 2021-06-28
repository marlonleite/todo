from rest_framework import viewsets

from .models import TodoListModel
from .serializers import TodoListSerializer


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoListModel.objects.all()
    serializer_class = TodoListSerializer
    http_method_names = ("get", "post", "patch", "delete")
