"""URL configuration for the accounts app. The project's urls.py includes these addresses under accounts/."""

from django.urls import include, path

from . import views

app_name = "accounts"

urlpatterns = [
    # Django's built-in login and logout pages: login/, logout/, password change, and so on.
    path("", include("django.contrib.auth.urls")),
    # Our registration page, for creating a new account.
    path("register/", views.register, name="register"),
]
