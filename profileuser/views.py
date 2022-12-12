from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from profileuser.models import *
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.core import serializers
from django.template import loader
from django.urls import reverse
from profileuser.forms import UserImageForm
from django.contrib.auth.decorators import login_required
from arti.models import * 
from beli_karya.models import *
import json
from django.views.decorators.csrf import requires_csrf_token
from django.http import JsonResponse

# Create your views here.

@login_required(login_url='/login')
def show_profile(request):
    profile = Profile.objects.filter(user=request.user).last()
    profileimg = UploadImage.objects.filter(user=request.user).last()
    profileimg2 = Karya.objects.filter(user=request.user)
    imgbeli = Transaksi.objects.filter(user=request.user)
    donasi = 0
    for jumlahDonasi in imgbeli:
        if jumlahDonasi.karya.sudah_dibeli == True:
            donasi += jumlahDonasi.karya.harga

    template = loader.get_template('profile.html')

    context = {
        'changes' : profile,
        'img' : profileimg,
        'img2' : profileimg2,
        'imgbeli' : imgbeli,
        'donasi' : donasi,

    }
    
    return HttpResponse(template.render(context, request))

def add(request):
    profile = Profile.objects.filter(user=request.user).last()
    profileimg = UploadImage.objects.filter(user=request.user).last()
    profileimg2 = Karya.objects.filter(user=request.user)
    imgbeli = Transaksi.objects.filter(user=request.user)

    template = loader.get_template('add.html')

    context = {
        'changes' : profileValue,
        'img' : profileimg,
        'img2' : profileimg2,
        'imgbeli' : imgbeli,

    }
    return HttpResponse(template.render(context, request)) 

@login_required(login_url='/login')
def show_edit_profile(request):
    username1 = request.POST['username']
    email1 = request.POST['email']
    phone1 = request.POST['phone']
    mobile1 = request.POST['mobile']
    address1 = request.POST['address']
    profile1 = Profile(
        user=request.user,
        username = username1,
        email = email1,
        phone = phone1,
        mobile = mobile1,
        address = address1)
        
    if(len(Profile.objects.filter(user=request.user)) < 1):
        profile1.save()

    else:
        Profile.objects.filter(user=request.user).delete()
        profile1.save() 

    return HttpResponseRedirect(reverse('profileuser:show_profile'))

@login_required(login_url='/login')
def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():
            form.instance.user = request.user
            if(len(UploadImage.objects.filter(user=request.user)) < 1):
                form.save()

            else:
                UploadImage.objects.filter(user=request.user).delete()
                form.save()     
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'edit_profile.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImageForm()  
  
    return render(request, 'edit_profile.html', {'form': form})  

# def get_json(request):
#     dataprofile = Profile.objects.last()
#     return HttpResponse(serializers.serialize("json", dataprofile), content_type="application/json")

@login_required(login_url='/login')
def show_ajax_profile(request):
    profile = Profile.objects.filter(user=request.user).last()
    profileimg = UploadImage.objects.filter(user=request.user).last()     
    profileimg2 = Karya.objects.filter(user=request.user)
    imgbeli = Transaksi.objects.filter(user=request.user)

    template = loader.get_template('edit_ajax_profile.html')

    context = {
        'changes' : profile,
        'img' : profileimg,
        'img2' : profileimg2,
        'imgbeli' : imgbeli,
    }
    return HttpResponse(template.render(context, request))

def show_json_profile(request):
    dataProfile = Profile.objects.all()
    lst = []
    for data in dataProfile:
        lst.append({
            'username': data.username,
            'email' : data.email,
            'phone' : data.phone,
            'address' : data.address,
        })
    return HttpResponse(json.dumps(lst), content_type="application/json")

def show_json_profile_img(request):
    dataProfileImg = UploadImage.objects.all()
    lst = []
    for data in dataProfileImg:
        lst.append({
            'image' : data.image.url
        })
    return HttpResponse(json.dumps(lst), content_type="application/json")

def show_json_profile_img2(request):
    dataProfileImg2 = Karya.objects.all()
    lst = []
    for data in dataProfileImg2:
        lst.append({
            'gambar' : data.gambar.url,
            'judul' : data.judul,
        
        })
    return HttpResponse(json.dumps(lst), content_type="application/json")
    
def show_json_profile_imgbeli(request):
    dataProfileImgBeli = Transaksi.objects.all()
    lst = []
    donasi = 0
    for jumlahDonasi in dataProfileImgBeli:
        if jumlahDonasi.karya.sudah_dibeli == True:
            if (len(lst) > 0):
                lst.clear()
            donasi += jumlahDonasi.karya.harga
            lst.append({
                'donasi' : donasi
            })
    
    return HttpResponse(json.dumps(lst), content_type="application/json")

@requires_csrf_token
def show_json_profile_save(request):
    lst = []
    if (request.method == 'POST'):
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        profile = Profile(
            user=request.user,
            username = username,
            email = email,
            phone = phone,
            mobile = mobile,
            address = address)

        profile.save()

        lst.append(profile)
        
    # if(len(Profile.objects.all()) < 1):
    #     profile.save()

    # else:
    #     Profile.objects.all().delete()
    #     profile.save() 

        return HttpResponse(serializers.serialize("json", profile), content_type="application/json")
    return HttpResponse(json.dumps(lst), content_type="application/json")