from django.urls import path
from leaderboard.views import show_leaderboard
from leaderboard.views import create_review

app_name = 'leaderboard'

urlpatterns = [
    path('', show_leaderboard, name='show_leaderboard'),
    path('create-review/', create_review, name='create_review'),
]