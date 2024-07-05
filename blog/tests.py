from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post, Comment, Category,User

# class PostModelTest(TestCase):
#     def setUp(self):
#         self.category = Category.objects.create(name="Django")
#         self.author = User.objects.create(username="testuser", email="test@example.com", password="testpass")
#         self.post = Post.objects.create(
#             title="Test Post",
#             content="This is a test post.",
#             author=self.author,
#             category=self.category
#         )

#     def test_post_creation(self):
#         self.assertEqual(self.post.title, "Test Post")
#         self.assertEqual(self.post.author.username, "testuser")
#         self.assertEqual(self.post.category.name, "Django")

# class PostAPITest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.category = Category.objects.create(name="Django")
#         self.author = User.objects.create(username="testuser", email="test@example.com", password="testpass")
#         self.post = Post.objects.create(
#             title="Test Post",
#             content="This is a test post.",
#             author=self.author,
#             category=self.category
#         )

#     def test_get_posts(self):
#         response = self.client.get('/api/posts/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_create_post(self):
#         data = {
#             "title": "New Post",
#             "content": "This is a new post.",
#             "author": self.author.id,
#             "category": self.category.id
#         }
#         response = self.client.post('/api/posts/', data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CommentModelTest(TestCase):
    def setUp(self):
        # self.category = Category.objects.create(name="Django")
        self.author = User.objects.create(username="testuser", email="test@example.com", password="testpass")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.author,
            # category=self.category
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.author,
            content="This is a test comment."
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.content, "This is a test comment.")
        self.assertEqual(self.comment.post.title, "Test Post")
        self.assertEqual(self.comment.author.username, "testuser")
