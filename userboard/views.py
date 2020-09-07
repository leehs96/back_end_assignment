from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def index(request):
    posts = Post.objects
    return render(request, 'index.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post})

def create(request):
    if request.method == "POST":
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.time = timezone.datetime.now()
        post.author = request.user
        post.save()
        return redirect('index')
    
    else:
        return render(request, 'create.html')

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.time = timezone.datetime.now()
        post.save()
        return redirect('detail', post.id) 

    else:
        return render(request, 'update.html', {'post': post})

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        return redirect('index')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'login_error': 'Wrong!!'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')