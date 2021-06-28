from django.db import transaction
from rest_framework import serializers

from .models import TodoListModel


class TodoListSerializer(serializers.ModelSerializer):
    done = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        model = TodoListModel
        fields = ("id", "title", "done")

    @transaction.atomic
    def create(self, validated_data):
        if self.Meta.model.objects.all().count() >= 5:
            raise serializers.ValidationError(
                {"error": "No more than five tasks are allowed."}
            )
        self.Meta.model.objects.create(**validated_data)
        return validated_data

    @transaction.atomic
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.done = validated_data.get("done", instance.done)
        instance.save()
        return instance

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["done"] = getattr(instance, "done", False)
        return ret
