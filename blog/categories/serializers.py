from blog.models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = [
            "id",
        ]

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                f"name length must be bigger than 3. current lenght is {len(value)}."
            )
        return value
