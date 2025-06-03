from django.contrib import admin

from .models import Topic, Entry # look in same directory as admins.py

admin.site.register(Topic)
admin.site.register(Entry)