from django.forms import ModelForm
from .models import Karya

class FormKarya(ModelForm):
    class Meta:
        model = Karya
        fields = ('gambar', )
        labels = {
            'gambar': '',
        }
        widgets = {
            
        }