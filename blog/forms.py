from django import forms
from django.forms import ModelForm

from . models import Post

class PostForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = '__all__'
        exclude = ['date_posted']
        