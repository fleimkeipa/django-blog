from rest_framework import serializers
from blog.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["id", "created_at", "author", "post"]

    def create(self, validated_data):
        # add user in validated data on request context
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
