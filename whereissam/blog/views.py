# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ProfileForm, CommentForm
from .models import Comment
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatisch inloggen
            return redirect('post_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by("-created_at")

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect("post_detail", slug=post.slug)
        else:
            return redirect("login")
    else:
        form = CommentForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form,
    })

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        return HttpResponseForbidden("Je mag deze reactie niet bewerken.")

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail", slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, "blog/comment_form.html", {"form": form, "comment": comment})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        return HttpResponseForbidden("Je mag deze reactie niet verwijderen.")

    if request.method == "POST":
        post_slug = comment.post.slug
        comment.delete()
        return redirect("post_detail", slug=post_slug)

    return render(request, "blog/comment_confirm_delete.html", {"comment": comment})

@login_required
def profile(request):
    user = request.user

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # refresh de pagina na opslaan
    else:
        form = ProfileForm(instance=user)

    return render(request, 'accounts/profile.html', {'form': form})