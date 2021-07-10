from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from blog.models import Post

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #to get registered users username
            messages.success(request, f'Accoutn created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request, 'users/register.html', context)

def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog-home')

    context = {}
    return render(request, 'users/login.html', context)   

def logoutPage(request):
    logout(request)
    messages.success(request, f'You now have loged out!')
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        #my_post = Post.objects.filter(author=request.user)
        


    context = {
        'u_form': u_form,
        'p_form': p_form,
        #'my_post':my_post,
    }
    return render(request, 'users/profile.html', context)    

      



