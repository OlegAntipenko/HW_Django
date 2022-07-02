from django import forms
from django.forms import ModelForm

from .models import *


class BookAdd(forms.Form):
    title = forms.CharField(max_length=100, label="Введите название книги")
    description = forms.CharField(widget=forms.Textarea, label="Введите описание книги")
    author = forms.ModelChoiceField(queryset=Authors.objects.all(), label="Выберите автора",
                                    empty_label="Автор не выбран")

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

