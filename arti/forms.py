from django.forms import *
from .models import Karya

class FormKarya(ModelForm):
    class Meta:
        model = Karya
        fields = ('gambar', 'judul', 'harga', 'deskripsi')
        labels = {
            'gambar': '',
            'judul': '',
            'harga': '',
            'deskripsi': '',
        }
        widgets = {
            'judul': TextInput(attrs={'class':'form-control', 'placeholder':'Judul Karya'}),
            'harga': TextInput(attrs={'class':'form-control', 'placeholder':'Harga (Rp)'}),
            'deskripsi': Textarea(attrs={'class':'form-control', 'placeholder':'Deskripsi', 'cols': 40, 'rows': 10}),
        }