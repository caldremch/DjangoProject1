from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    class Meta:
        verbose_name = u'分类目录'
        verbose_name_plural = u'分类目录'

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签'

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # 标签
    tags = models.ManyToManyField(Tag)
    # 分类目录
    category = models.ForeignKey(Category,null=True)
    # 点击量
    click = models.IntegerField(default=0)
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

@python_2_unicode_compatible
class Comment(models.Model):
    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'
    author = models.CharField(max_length=20)
    email = models.EmailField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post)

    def __str__(self):
        return '{0}: {1}'.format(self.author, self.post.title)
@python_2_unicode_compatible
class Comment(models.Model):
    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'
    author = models.CharField(max_length=20)
    email = models.EmailField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post)

    def __str__(self):
        return '{0}: {1}'.format(self.author, self.post.title)
