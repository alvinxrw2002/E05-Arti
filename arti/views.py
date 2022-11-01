import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Karya, UserArti
from .forms import FormKarya

# Create your views here.
def index(request):
    user = "guest"
    if request.user.is_authenticated:
        user = request.user
    return render(request, 'index.html', {'user': user})

def galeri(request):
    loggedin_user = request.user
    if loggedin_user.is_superuser or not loggedin_user.is_authenticated:
        context = {
        'user': loggedin_user,
        'karyas': Karya.objects.all()
        }
        return render(request, 'galeri.html', context)

    user_arti = UserArti.objects.get(user=loggedin_user)
    objects = Karya.objects.filter(kategori=user_arti.kategori_favorit)
    context = {
        'user' : loggedin_user,
        'user_arti' : user_arti,
        'karyas' : objects
    }

    return render(request, 'galeri.html', context)

def login_user(request):
    if request.user:
        logout_user(request)

    if request.method == 'POST':
        # Autentikasikan username dan password
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("arti:index")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')

    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_kategori = request.POST.get('kategori')
            new_user_arti = UserArti(user = new_user, kategori_favorit = new_kategori)
            new_user_arti.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('arti:login')

    return render(request, 'register.html', {'form': form})

@login_required(login_url='/login')
def logout_user(request):
    # Redirect ke halaman login dan hapus cookie
    logout(request)
    response = HttpResponseRedirect(reverse('arti:index'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def post_karya(request):
    if request.method == 'POST':
        form = FormKarya(request.POST, request.FILES)
        if form.is_valid():
            karya = form.save(commit=False)
            karya.user = request.user
            karya.save()
            return redirect('arti:galeri')

    # jika method-nya GET atau yang lainnya, buat form kosong
    else:
        form = FormKarya()

    # Tampilkan form baru
    return render(request, 'post-karya.html', {'form': form})

@login_required(login_url='/login')
def delete_karya(request, karya_id):
    karya_dihapus = Karya.objects.get(pk = karya_id)
    if karya_dihapus.gambar:
        karya_dihapus.gambar.delete()
    karya_dihapus.delete()
    return HttpResponse("success")

@login_required(login_url='/login')
@csrf_exempt
def edit_karya(request, karya_id):
    karya_edit = Karya.objects.get(pk = karya_id)
    karya_edit.judul = request.POST["judul"]
    karya_edit.kategori = request.POST["kategori"]
    karya_edit.harga = request.POST["harga"]
    karya_edit.deskripsi = request.POST["deskripsi"]
    karya_edit.save()
    return HttpResponse("success")
