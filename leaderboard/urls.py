from django.urls import path
from leaderboard.views import show_leaderboard
from leaderboard.views import create_comment
from leaderboard.views import leaderboard_pengguna
from leaderboard.views import change_comments

app_name = 'leaderboard'

urlpatterns = [
    path('', show_leaderboard, name='show_leaderboard'),
    path('create-comment/', create_comment, name='create_comment'),
    path('leaderboard-pengguna', leaderboard_pengguna, name="leaderboard_pengguna"),
    path('change-comments', change_comments, name="change_comments")
]