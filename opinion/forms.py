from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.db import models

from opinion.models import opinion

from django import forms
from django.forms import ModelForm


class opinion_form(forms.ModelForm):

    class Meta:
        model = opinion
        fields = '__all__'
		
	
class register_form(UserCreationForm):
	
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	
	class Meta:
		model=User
		fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
