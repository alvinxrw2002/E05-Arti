from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from arti.models import *

from django.db.models.fields.files import ImageFieldFile
from django.http import HttpResponse, JsonResponse
from django.core import serializers


@login_required(login_url='/login')
def get_object_karya_json(request) :
    loggedin_user = request.user
    if loggedin_user.is_superuser:
        karya = Karya.objects.all()
        return HttpResponse(serializers.serialize("json", karya), content_type="application/json")

    user_arti = UserArti.objects.get(user=loggedin_user)
    karya = Karya.objects.filter(kategori=user_arti.kategori_favorit)
    data = []
    for item in karya :
        data.append(
            {"pk": item.pk, 
            "fields": {"user_loggedin": loggedin_user.id, "user": item.user.id, "gambar" : encode_datetime(item.gambar), "judul" : item.judul,
            "kategori" : item.kategori, "harga": item.harga, "deskripsi": item.deskripsi,
            "tanggal": item.tanggal}})
    data = {'data' : data}
    print(data)
    return JsonResponse(data)

@login_required(login_url='/login')
def show_galeri(request):
    return render(request, 'show_galeri.html')

@login_required(login_url='/login')
def delete_karya(request, id) :
    karya_dihapus = Karya.objects.get(pk = id)
    if karya_dihapus.gambar:
        karya_dihapus.gambar.delete()
    karya_dihapus.delete()
    return HttpResponse("success")

def encode_datetime(obj):
    if isinstance(obj, ImageFieldFile):
        try:
            return obj.path
        except ValueError:
            return ''

    raise TypeError(repr(obj) + " is not JSON serializable")