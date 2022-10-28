from django.shortcuts import render
from leaderboard.models import Review
from django.contrib.auth.models import User
from leaderboard.forms import ReviewForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers

# Create your views here.
# @login_required(login_url='/login/')
def show_leaderboard(request):
    new_form = ReviewForm()
    reviews = Review.objects.all()
    users = User.objects.all()
    context = {
        'reviews': reviews,
        'users' : users,
        'form' : new_form,
    }
    return render(request, 'leaderboard.html', context)
    
def create_review(request):
    form = ReviewForm(request.POST)
    if form.is_valid():
       review = form.save(commit=False)
       review.user = request.user
       review.save()
    return redirect('leaderboard:show_leaderboard')

def leaderboard_pengguna(request):
    users = list(User.objects.all().order_by("pk"))
    users = users[:10]
    context={
        "users": users,
    }
    return render(request, "leaderboard_pengguna.html", context)