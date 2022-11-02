from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from arti.models import Karya
from beli_karya.models import Transaksi
import json

# Create your views here.
def get_karyas(request):
    karyas = Karya.objects.all()
    lst = []
    for karya in karyas:
        transaksi = Transaksi.objects.filter(karya = karya)
        lst.append({
            'id': karya.pk,
            'judul': karya.judul,
            'kategori': karya.kategori,
            'deskripsi': karya.deskripsi,
            'user': karya.user.username,
            'harga': karya.harga,
            'tanggal': karya.tanggal.strftime('%d %B %Y'),
            'gambar': karya.gambar.url,
            'sudah_dibeli': transaksi.exists()
        })
    return HttpResponse(json.dumps(lst), content_type='application/json')

@login_required(login_url='/login')
def beli_karya(request):
    loggedin_user = request.user
    context = {
        'user': loggedin_user,
    }
    if request.method == 'POST':
        karyas = request.POST.getlist('karyas[]')
        print(karyas)
        for karya in karyas:
            k = Karya.objects.get(pk=int(karya))
            transaksi = Transaksi(user=loggedin_user, karya = k)
            transaksi.save()
    return render(request, 'beli-karya.html', context)
