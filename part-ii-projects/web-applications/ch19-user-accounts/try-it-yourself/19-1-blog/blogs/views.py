"""The views for the blogs app. A view receives a request and returns a response."""

from django.shortcuts import get_object_or_404, redirect, render

from .forms import BlogForm, BlogPostForm
from .models import Blog, BlogPost


def index(request):
    """The home page: every post, newest first, with links to add a post to each blog."""
    posts = BlogPost.objects.select_related("blog").all()
    blogs = Blog.objects.all()
    context = {"posts": posts, "blogs": blogs}
    return render(request, "blogs/index.html", context)


def new_blog(request):
    """Make a new blog. On a GET request, show an empty form."""
    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    context = {"form": form}
    return render(request, "blogs/new_blog.html", context)


def new_post(request, blog_id):
    """Write a new post in a blog. The post is linked to the blog it was written in."""
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method != "POST":
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            # Build the post, but don't save it yet, so the blog can be added first.
            new_post_record = form.save(commit=False)
            new_post_record.blog = blog
            new_post_record.save()
            return redirect("blogs:index")

    context = {"blog": blog, "form": form}
    return render(request, "blogs/new_post.html", context)


def edit_post(request, post_id):
    """Edit an existing post."""
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method != "POST":
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    context = {"post": post, "form": form}
    return render(request, "blogs/edit_post.html", context)
