from django import forms
from leaderboard.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        labels = {'text':'Input Text'}
        widgets = {
            'text' : forms.Textarea(attrs={'cols' : 5, 'rows' : 5, 'class':'form-control'})
        }