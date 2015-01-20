__author__ = 'KATE'
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Comments


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['ctext']


class Registration(ModelForm):
    class Meta:
        model = User
