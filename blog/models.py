from django.db import models
from django.contrib.auth.models import User


"""
{
    "name":"category name"
}
"""


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


"""
{
    "author":1,
    "categories": [
        {
            "id":2,
            "name":"category 1"
        }
    ],
    "title": "post title",
    "content": "post content",
}
    "created_at":fill auto when created,
    "updated_at":fill auto when updated,
"""


class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name="posts_categories")
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


"""
{
    "author": 1,
    "post": 6,
    "content": "aaa"
}
"""


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
