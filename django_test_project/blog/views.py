from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'blog/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            return render(request, 'blog/post_form.html', {'form': form})


def home(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
        'title': 'Zen of Python'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')