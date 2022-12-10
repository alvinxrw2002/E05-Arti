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
    path('profile-json', show_json_profile, name='show_json_profile'),
    path('profile-img-json', show_json_profile_img, name='show_json_profile_img'),
    path('profile-img2-json', show_json_profile_img2, name='show_json_profile_img2'),
    path('profile-imgbeli-json', show_json_profile_imgbeli, name='show_json_profile_imgbeli'),

]
