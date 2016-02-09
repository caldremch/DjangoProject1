from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # 定义一个元类
    class Meta:
        model = Post
        fields = ('title', 'text')