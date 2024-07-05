from blog.models import Category, Post, Comment
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User


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


class PostSerializer(serializers.ModelSerializer):
    posts_categories = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="category-detail",
    )

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "author"]

    def create(self, validated_data):
        # add user in validated data on request context
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                f"title length must be bigger than 3. current lenght is {len(value)}."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="author-detail",
    )

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["id"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
