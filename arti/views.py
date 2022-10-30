import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Karya, UserArti
from .forms import FormKarya

# Create your views here.
@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login')
def galeri(request):
    loggedin_user = request.user
    if loggedin_user.is_superuser:
        context = {
        'user': loggedin_user,
        'karyas': Karya.objects.all()
        }
        return render(request, 'galeri.html', context)

    user_arti = UserArti.objects.get(user=loggedin_user)
    objects = Karya.objects.filter(kategori=user_arti.kategori_favorit)
    for i in range(1000):
        print(objects)
    context = {
        'user' : loggedin_user,
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

    return render(request, 'register.html')

@login_required(login_url='/login')
def logout_user(request):
    # Redirect ke halaman login dan hapus cookie
    logout(request)
    response = HttpResponseRedirect(reverse('arti:login'))
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
            return redirect('arti:index')

    # jika method-nya GET atau yang lainnya, buat form kosong
    else:
        form = FormKarya()

    # Tampilkan form baru
    return render(request, 'post-karya.html', {'form': form})
