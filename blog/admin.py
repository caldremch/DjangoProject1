from django.contrib import admin

# Register your models here.
#after register models
#manage models through the admin

#.相对路径导入
from .models import Post
admin.site.register(Post)