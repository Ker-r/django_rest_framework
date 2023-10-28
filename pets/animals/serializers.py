from rest_framework import serializers
from .models import Animal


# class AnimalModel:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description


# class AnimalSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     description = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     category_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Animal.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.description = validated_data.get("description", instance.description)
#         instance.time_update = validated_data.get("time_create", instance.time_create)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.category_id = validated_data.get("category_id", instance.category_id)
#         instance.save()
#         return instance

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ("title", "description", "category")
        