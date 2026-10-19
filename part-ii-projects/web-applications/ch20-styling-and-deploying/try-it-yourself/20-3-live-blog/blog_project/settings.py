"""
Settings for the Blog project, ready for a live server.

These are the 20-2 settings, with the values that change on a live site read from environment variables. Locally the
defaults work without any setup. The variable names match the Learning Log's, so the deployment steps are the same.
"""

import os
from pathlib import Path

# Build paths inside the project, such as BASE_DIR / 'templates'.
BASE_DIR = Path(__file__).resolve().parent.parent

# The secret key signs sessions and passwords. A live site sets LL_SECRET_KEY; the default is for learning only.
SECRET_KEY = os.environ.get("LL_SECRET_KEY", "django-insecure-blog-project-training-key-change-before-deploying")

# Debug mode shows detailed error pages. It's on locally, and a live site sets LL_DEBUG to 0.
DEBUG = os.environ.get("LL_DEBUG", "1") == "1"

# The addresses the site answers to. Locally that's this computer. A live site adds its own address in LL_ALLOWED_HOSTS.
ALLOWED_HOSTS = ["127.0.0.1", "localhost"] + [
    host.strip() for host in os.environ.get("LL_ALLOWED_HOSTS", "").split(",") if host.strip()
]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps: Bootstrap helpers for styling the pages.
    "django_bootstrap5",
    # Our apps: blogs and their posts, and the accounts for signing in.
    "blogs",
    "accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "blog_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "blog_project.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Accounts: where to go after signing in and out.

LOGIN_REDIRECT_URL = "blogs:index"
LOGOUT_REDIRECT_URL = "blogs:index"


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files: on a live site, collectstatic gathers them into STATIC_ROOT, so the web server can serve them.

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
