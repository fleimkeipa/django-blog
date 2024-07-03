from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from blog.serializers import AuthorSerializer
from rest_framework.permissions import AllowAny


class Register(APIView):
    """
    User registration endpoint.
    """

    permission_classes = [AllowAny]  # Herhangi bir kullanıcı kaydı yapabilir

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            # hash the password
            serializer.validated_data["password"] = make_password(
                serializer.validated_data["password"]
            )
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorList(APIView):
    """
    List all authors or create a new author.
    """

    def get(self, request, format=None):
        authors = User.objects.all()
        serializer = AuthorSerializer(authors, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):
    """
    Retrieve, update or delete an author.
    """

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, id, format=None):
        author = self.get_object(id)
        serializer = AuthorSerializer(author, context={"request": request})
        return Response(serializer.data)

    def put(self, request, id, format=None):
        author = self.get_object(id)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        author = self.get_object(id)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
