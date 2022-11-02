from django.contrib import admin
from leaderboard.models import Comment, UserExtended
# Register your models here.
admin.site.register(Comment)
admin.site.register(UserExtended)