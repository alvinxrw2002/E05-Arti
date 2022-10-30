from django.urls import path
from profileuser.views import *

app_name = 'profileuser'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('edit/', add, name='add'),
    # path('json/', get_json, name='get_json'),
    path('edit/addimage/', image_request, name='image-request'),
    path('edit/addrecord/', show_edit_profile, name='show_edit_profile'),
    path('edit/profile-ajax/', show_ajax_profile, name='show_ajax_profile'),

]
