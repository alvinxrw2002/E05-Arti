from django.shortcuts import render
import datetime
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Pesan, Program
from django.http.response import JsonResponse
import json

# # Create your views here.
@login_required(login_url='/login')
def riwayat(request):
    data_donasi = Program.objects.all()
    context = {'data_donasi' : data_donasi}
    return render(request, "riwayat.html", context)

# def getData(request):
#     searchds = Program.objects.all()
#     searchds_list = serializers.serialize('json', searchds)
#     return HttpResponse(searchds_list, content_type="text/json-comment-filtered")

# Create your views here.

def list_donatur(request, program):
    donasi_terkumpul = Program.objects.get(pk=program)
    response = {
        'donasi_terkumpul': donasi_terkumpul,
        }
    return render(request, 'riwayat.html', response)

def pesan(request):
    username = 'anon'
    if request.user.is_authenticated:
        username = request.user
        # print(username)

    if request.POST:
        nama = username
        isi = request.POST.get('isi')
        Pesan.objects.create(nama=nama, isi=isi)
        return HttpResponseRedirect('/riwayat/')
        
    else:
        form = FormPesan()
        Pesans = Pesan.objects.all()

        for Pesan in Pesans:
            print(Pesan)
        
        context = {
            'Pesans':Pesans,
            'form':form
        }
        return render(request, 'riwayat.html', context)

def pesanajax(request):
    argument = request.GET['q']
    username = request.user
    Pesan.objects.create(nama=username, isi=argument)
    datastr = serializers.serialize("json", Pesan.objects.all())
    data = json.loads(datastr)

    return JsonResponse(data, safe=False)