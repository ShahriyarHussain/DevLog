# from django.forms import ModelForm
from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['content', 'post', 'author']
