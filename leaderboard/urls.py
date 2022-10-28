from django.urls import path
from leaderboard.views import show_leaderboard
from leaderboard.views import create_review
from leaderboard.views import leaderboard_pengguna

app_name = 'leaderboard'

urlpatterns = [
    path('', show_leaderboard, name='show_leaderboard'),
    path('create-review/', create_review, name='create_review'),
    path('leaderboard-pengguna', leaderboard_pengguna, name="leaderboard_pengguna")
]