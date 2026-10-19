"""
Settings for the Learning Log project.

Django's settings file. Everything the project needs to run is set here: the apps it uses, the database, the
templates, and the static files.

Values that change for the live site are read from environment variables, so the real secret key never goes into the code.
Locally the defaults work without any setup, so the runner and the tests need no changes.
"""

import os
from pathlib import Path

# Build paths inside the project, such as BASE_DIR / 'templates'.
BASE_DIR = Path(__file__).resolve().parent.parent

# The secret key signs sessions and passwords. The live site sets LL_SECRET_KEY; the default is for learning only.
SECRET_KEY = os.environ.get("LL_SECRET_KEY", "django-insecure-learning-log-training-key-change-before-deploying")

# Debug mode shows detailed error pages. It's on locally, and the live site sets LL_DEBUG to 0.
DEBUG = os.environ.get("LL_DEBUG", "1") == "1"

# The addresses the site answers to. Locally that's this computer. On the live site, LL_ALLOWED_HOSTS lists the
# student's own address, such as username.pythonanywhere.com, separated by commas.
ALLOWED_HOSTS = ["127.0.0.1", "localhost"] + [
    host.strip() for host in os.environ.get("LL_ALLOWED_HOSTS", "").split(",") if host.strip()
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps: Bootstrap helpers for styling the pages.
    "django_bootstrap5",
    # Our apps: the topics and entries, and the accounts for signing in.
    "learning_logs",
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

ROOT_URLCONF = "ll_project.urls"

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

WSGI_APPLICATION = "ll_project.wsgi.application"


# Database
# The database is a single file, db.sqlite3, which Django creates when you run migrate.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Accounts: where to go after signing in and out.

LOGIN_REDIRECT_URL = "learning_logs:index"
LOGOUT_REDIRECT_URL = "learning_logs:index"


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# On the live site, collectstatic gathers every static file into STATIC_ROOT, so the web server can serve them.

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
