import datetime
from django.urls                    import reverse
from django.contrib                 import messages
from django.http                    import HttpResponseRedirect
from django.shortcuts               import render, redirect
from django.contrib.auth            import authenticate, login, logout
from django.contrib.auth.forms      import UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('/login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

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

def logout_user(request):
    # Redirect ke halaman login dan hapus cookie
    logout(request)
    response = HttpResponseRedirect(reverse('arti:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html', {'user': request.user})
