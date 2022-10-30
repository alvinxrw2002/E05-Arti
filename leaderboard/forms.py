from django import forms
from leaderboard.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text':'Input Text'}
        widgets = {
            'text' : forms.Textarea(attrs={'cols' : 32, 'rows' : 5, 'class':'form-control'})
        }