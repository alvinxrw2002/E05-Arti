from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from profileuser.models import *
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
from profileuser.forms import UserImageForm
from arti.models import *  

# Create your views here.

def show_profile(request):
    profile = Profile.objects.last()
    profileimg = UploadImage.objects.last()
    profileimg2 = Karya.objects.all()

    template = loader.get_template('profile.html')

    context = {
        'changes' : profile,
        'img' : profileimg,
        'img2' : profileimg2,

    }
    return HttpResponse(template.render(context, request))

def add(request):
    profileValue = Profile.objects.last()
    profileimg = UploadImage.objects.last()
    profileimg2 = Karya.objects.all()
    template = loader.get_template('add.html')

    context = {
        'changes' : profileValue,
        'img' : profileimg,
        'img2' : profileimg2,

    }
    return HttpResponse(template.render(context, request)) 

def show_edit_profile(request):
    username1 = request.POST['username']
    email1 = request.POST['email']
    phone1 = request.POST['phone']
    mobile1 = request.POST['mobile']
    address1 = request.POST['address']
    profile1 = Profile(
        username = username1,
        email = email1,
        phone = phone1,
        mobile = mobile1,
        address = address1)
        
    profile1.save()
    return HttpResponseRedirect(reverse('profileuser:show_profile'))

def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'edit_profile.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImageForm()  
  
    return render(request, 'edit_profile.html', {'form': form})  



