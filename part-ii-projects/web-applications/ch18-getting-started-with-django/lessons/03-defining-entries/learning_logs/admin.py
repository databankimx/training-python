"""Register the learning_logs models with the Django admin site."""

from django.contrib import admin

from .models import Entry, Topic

admin.site.register(Topic)
admin.site.register(Entry)
