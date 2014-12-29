__author__ = 'KATE'
from django.forms import ModelForm
from logsys.models import Registratin
from .models import Comments


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']


class Registration(ModelForm):
    class Meta:
        model = Registratin