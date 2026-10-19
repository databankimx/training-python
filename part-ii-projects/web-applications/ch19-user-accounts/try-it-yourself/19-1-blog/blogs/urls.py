"""URL configuration for the blogs app. The project's urls.py includes these addresses."""

from django.urls import path

from . import views

app_name = "blogs"

urlpatterns = [
    # The home page: every post, newest first.
    path("", views.index, name="index"),
    # The page for making a new blog.
    path("blogs/new/", views.new_blog, name="new_blog"),
    # The page for writing a new post in one blog. The number in the address is the blog's id.
    path("blogs/<int:blog_id>/new_post/", views.new_post, name="new_post"),
    # The page for editing one post. The number in the address is the post's id.
    path("posts/<int:post_id>/edit/", views.edit_post, name="edit_post"),
]
