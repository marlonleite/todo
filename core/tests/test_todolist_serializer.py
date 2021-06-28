import pytest

from core.serializers import TodoListSerializer


@pytest.mark.django_db
class TestTodoListSerializer:
    @pytest.mark.unit
    def test_serialize_model(self, data):
        serializer = TodoListSerializer(data)
        assert serializer.data

    @pytest.mark.unit
    def test_serialized_data(self, data):
        serializer = TodoListSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.errors == {}
