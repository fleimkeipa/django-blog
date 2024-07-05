from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from blog.models import Post, Comment
from blog.permissions import PostPermissions
from blog.serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


class PostList(generics.ListCreateAPIView):
    """
    List all posts and create new one.
    """

    queryset = Post.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("categories", "title")
    serializer_class = PostSerializer

    permission_classes = [PostPermissions]

    def get_queryset(self):
        return Post.objects.all()

    def get(self, request, format=None):
        queryset = self.get_queryset()

        # Filters
        filter_backend = DjangoFilterBackend()
        queryset = filter_backend.filter_queryset(request, queryset, self)

        # Pagination
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(
            result_page, many=True, context={"request": request}
        )

        return paginator.get_paginated_response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    """
    Retrieve, update or delete a post.
    """

    permission_classes = [PostPermissions]

    def get_object(self, pk):
        obj = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostComments(APIView):
    """
    List and create comments for a post.
    """

    permission_classes = [PostPermissions]

    def get_object(self, post_id):
        obj = get_object_or_404(Post, id=post_id)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, post_id, format=None):
        post = self.get_object(post_id)
        comments = Comment.objects.filter(post=post)

        # Pagination
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(comments, request)
        serializer = CommentSerializer(
            result_page, many=True, context={"request": request}
        )
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, post_id, format=None):
        post = self.get_object(post_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
