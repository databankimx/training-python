"""The views for the blogs app. A view receives a request and returns a response."""

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BlogForm, BlogPostForm
from .models import Blog, BlogPost


def index(request):
    """The home page: every post, newest first. Anyone can read the posts, signed in or not."""
    posts = BlogPost.objects.select_related("blog").all()
    blogs = Blog.objects.all()
    context = {"posts": posts, "blogs": blogs}
    return render(request, "blogs/index.html", context)


@login_required
def new_blog(request):
    """Make a new blog for the signed-in user. On a GET request, show an empty form."""
    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            # Build the blog, then record who owns it, before saving it.
            blog_record = form.save(commit=False)
            blog_record.owner = request.user
            blog_record.save()
            return redirect("blogs:index")

    context = {"form": form}
    return render(request, "blogs/new_blog.html", context)


@login_required
def new_post(request, blog_id):
    """Write a new post in one of the signed-in user's blogs."""
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.owner != request.user:
        raise Http404

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


@login_required
def edit_post(request, post_id):
    """Edit a post, but only if it's in one of the signed-in user's blogs. The check comes before the form is read."""
    post = get_object_or_404(BlogPost, id=post_id)
    if post.blog.owner != request.user:
        raise Http404

    if request.method != "POST":
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    context = {"post": post, "form": form}
    return render(request, "blogs/edit_post.html", context)
