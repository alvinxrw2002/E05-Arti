from django.shortcuts import render
from leaderboard.models import Comment
from django.contrib.auth.models import User
from leaderboard.forms import CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from arti.models import Karya
from django.http import HttpResponse
from django.core import serializers

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
       comment.username = request.user.username
       comment.save()
    return HttpResponse('Berhasil menambahkan comment baru!')

def change_comments(request):
    comments = Comment.objects.all()
    return HttpResponse(serializers.serialize("json", comments), content_type="application/json")

def leaderboard_pengguna(request):
    users = User.objects.all().order_by("pk")
    # context={
    #     "users": users,
    # }
    return HttpResponse(serializers.serialize("json", users), content_type="application/json")

def leaderboard_karya(request):
    karya = Karya.objects.all()
    context={
        "karya": karya,
    }
    return render(request, "leaderboard_karya.html", context)

def delete_comment(request):
    comment = Comment.objects.filter(pk=int(request.POST.get('id')))
    for cment in comment:
        cment.delete()
    return HttpResponse("Berhasil menghapus comment!")