from rest_framework import serializers
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="post-detail",
    )

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["id"]
