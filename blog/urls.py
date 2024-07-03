from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog.categories import views as category_views
from blog.posts import views as post_views
from blog.comments import views as comment_views
from blog.author import views as author_views

urlpatterns = [
    path("categories", category_views.category_list,name="category-list"),
    path("categories/<int:id>", category_views.category_detail, name="category-detail"),
    
    path("posts", post_views.PostList.as_view(),name="post-list"),
    path("posts/<int:pk>", post_views.PostDetail.as_view(), name="post-detail"),
    path("posts/<int:post_id>/comments", post_views.PostComments.as_view(),name="post-comments"),
    
    path("comments", comment_views.CommentList.as_view(),name="comment-list"),
    path("comments/<int:pk>", comment_views.CommentDetail.as_view(),name="comment-detail"),
    
    path("authors", author_views.AuthorList.as_view(),name="author-list"),
    path("authors/<int:id>", author_views.AuthorDetail.as_view(), name="author-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
