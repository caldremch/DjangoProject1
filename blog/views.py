#该文件是博客应用blog的

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.core.urlresolvers import reverse
# Create your views here.

#博客首页显示的文章列表
#这里显示的是已经发布了的文章,如果你new了一篇文章,在首页没显示出来,不用担心,那是因为它的published_date__isnull=True,因为
#在编写文章的时候,没有设置发布日期. 所以就有了草稿箱的出现
def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})

#文章详情
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

#request是上下文对象 传过来的,附带请求的信息
#新建文章
def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('blog.views.post_detail', pk = post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

#文章的编辑
def post_edit(request, pk):
    #根据pk值获取对象
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        #instance用于值的初始化
        form = PostForm(request.POST, instance=post)
        if form.is_valid():#is_valid是什么?
            post = form.save(commit=False)#保存这个表单
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk = post.pk)
    else:#如果没有提交
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})

#草搞箱
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts':posts})

#发布文章
def post_poblish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    #redirect重定向 当前目录的文件,可以留意一下和render的区别
    return redirect('blog.views.post_detail', pk)

#删除文章
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')