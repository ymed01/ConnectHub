from django.contrib import admin
from .models import Post, AgoraCredentials
# Register your models here.

admin.site.register(Post)
admin.site.register(AgoraCredentials)