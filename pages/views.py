from django.shortcuts import render, redirect, HttpResponse
from core.models import Post, Comment, Tag, User
from core.forms import CommentForm

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created')[:5]

    context = {
        'posts': posts,
    }

    return render(request, 'pages/index.html', context)

def post(request, pk):
    form = CommentForm()
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)

    context = {
        "post": post,
        "form": form,
        "comments": comments,
        }
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            return redirect('post', pk)

    return render(request, 'pages/post.html', context)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')