from rest_framework import status
from blog.models import Comment
from blog.permissions import CommentPermissions
from blog.serializers import CommentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


class CommentList(APIView):
    """
    List all comments.
    """

    permission_classes = [CommentPermissions]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("content",)

    def get_queryset(self):
        return Comment.objects.all()

    def get(self, request, format=None):
        queryset = self.get_queryset()

        # Filters
        filter_backend = DjangoFilterBackend()
        queryset = filter_backend.filter_queryset(request, queryset, self)

        # Pagination
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = CommentSerializer(
            result_page, many=True, context={"request": request}
        )
        return paginator.get_paginated_response(serializer.data)


class CommentDetail(APIView):
    """
    Retrieve, update or delete a comment.
    """

    permission_classes = [CommentPermissions]

    def get_object(self, pk):
        obj = get_object_or_404(Comment, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
