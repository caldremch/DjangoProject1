from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    #If True, the field is allowed to be blank. Default is False.
    # Note that this is different than null. null is purely database-related,
    #  whereas blank is validation-related. If a field has blank=True,
    # form validation will allow entry of an empty value.
    # If a field has blank=False, the field will be required.


    # null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空。
    # blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填，比如
    # published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

