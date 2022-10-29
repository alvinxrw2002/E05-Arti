from django.shortcuts import render
from leaderboard.models import Comment
from django.contrib.auth.models import User
from leaderboard.forms import CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
# @login_required(login_url='/login/')
def show_leaderboard(request):
    new_form = CommentForm()
    comment = Comment.objects.all()
    user = request.user
    context = {
        'comments': comment,
        'has_authenticated' : user.is_authenticated,
        'form' : new_form,
    }
    return render(request, 'leaderboard.html', context)
    
def create_comment(request):
    form = CommentForm(request.POST)
    if form.is_valid():
       comment = form.save(commit=False)
       comment.user = request.user
       comment.save()
    return HttpResponse('success')

def change_comments(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments,
    }
    return render(request, 'comments_carousel.html', context)

def leaderboard_pengguna(request):
    users = list(User.objects.all().order_by("pk"))
    users = users[:10]
    context={
        "users": users,
    }
    return render(request, "leaderboard_pengguna.html", context)