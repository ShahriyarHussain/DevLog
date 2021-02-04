# from django.forms import ModelForm
from django import forms
from .models import Comment_table


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment_table
        fields = ['comment']
