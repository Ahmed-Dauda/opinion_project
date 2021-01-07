from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect

from django.urls import reverse

from opinion.forms import *

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth  import authenticate, login, logout as django_logout

from opinion.forms import opinion_form

# Create your views here.

def index_view(request):
	
	
	form =register_form()
	
	if request.method=='POST':
		form =register_form(request.POST)
		if form.is_valid():
			form.save()
			form=AuthenticationForm()
			return  render(request,'opinion/signin.html', {'form':form, 'mm': 'You have Successfully Registered. You can now log In'})
			
		else:
			
			form =register_form()
			context={
			'form':form,
			'm':'unsuccessful registration; password, mismatched. Try again.'.title()
			}
			
			return render(request,'opinion/index.html', context)
		
			
	else:
		form =register_form()
		
		context={'form':form}
		return render(request,'opinion/index.html', context)
	
	
def register_view(request):
	form = opinion_form()
	if request.method=='POST':
			form = opinion_form(request.POST)
			if form.is_valid():
				form.save()
				return redirect('logout')

				
	else:
			
			form = opinion_form()
			
		
	context={
	'form':form
	}
	return  render(request, 'opinion/register.html', context)
	
	
def signin_view(request):
	form = AuthenticationForm()
	if request.method=='POST':
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			if user is not None:
				login(request, user)
				return redirect('register')
				
				
			else:
				form=AuthenticationForm()
		return  render(request,'opinion/signin.html', {'form':form, 'm':'Invalid Login Details'}) 
								
	else:
		form=AuthenticationForm()
		return  render(request,'opinion/signin.html', {'form':form})		
		
	
def logout_view(request):
	django_logout(request)
	return  render(request,'opinion/logout.html')
