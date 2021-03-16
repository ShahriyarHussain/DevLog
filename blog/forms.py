# from django.forms import ModelForm
from django import forms
# from tinymce import TinyMCE
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = ['content', 'post', 'author']
        fields = ['content']
