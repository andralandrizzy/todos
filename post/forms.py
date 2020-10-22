from django import forms
from django.forms import ModelForm
from . models import *

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

# class TaskForm(forms.Form):
#     title = forms.CharField(label='Enter task title', max_length=200)
#     description = forms.CharField(label='Task descriptions', max_length=300)
#     complete = forms.BooleanField(required=False)
