from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from . forms import *
from django.contrib import messages



# Create your views here.
@login_required(login_url='login')
def home(request):
    posts = Post.objects.all()
    
    #search filter
    post_name = request.GET.get('post_name')
    if post_name != '' and post_name is not None:
        posts = posts.filter(title__icontains=post_name)

    #pagination
    paginator = Paginator(posts, 4)
    page= request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'posts':posts}
    return render(request, 'blog/home.html', context)
    

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})   

@login_required(login_url='login')
def createPost(request, pk):
    author = User.objects.get(id=pk)
    form = PostForm(initial={'author':author}) #instance
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Post is created successfully')
            return redirect('blog-home')

    context={'form':form}
    return render(request, 'blog/post_form.html', context)  

def myPost(request):
    my_post = Post.objects.filter(author=request.user)
    
    context = {'my_post':my_post}
    return render(request, 'blog/my_post.html', context)   

def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Post is updated successfully')
            return redirect('my-post')

    context={'form':form}
    return render(request, 'blog/update_post.html', context)  

def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, f'Your Post is deleted successfully')
        return redirect('my-post')

    context={'post':post}
    return render(request, 'blog/delete_post.html', context)      

