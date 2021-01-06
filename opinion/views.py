from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect

from opinion.forms import *

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth  import authenticate, login, logout as django_logout

from opinion.forms import opinion_form

# Create your views here.

def index_view(request):
	
	if request.method=='POST':
		form =opinion_form(request.POST)
		if form.is_valid():
			form.save()
			return
			redirect('logout')
			
		else:
			return redirect('index')
			
			
	else:
		form =opinion_form()
		
		context={'form':form}
		return render(request,'opinion/index.html', context)
	
def signup_view(request):
	form = register_form()
	if request.method=='POST':
			form = register_form(request.POST)
			if form.is_valid():
				form.save()
				username=form.cleaned_data.get('username')
				password=form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password )
			login(request, user)
			return redirect('/')
				
	else:
			
			form = register_form()
			
		
	context={
	'form':form
	}
	return  render(request, 'opinion/signup.html', context)
	
def signin_view(request):
	form = AuthenticationForm()
	if request.method=='POST':
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			if user is not None:
				login(request, user)
				return redirect('index')
				
				
			else:
				form=AuthenticationForm()
		return  render(request,'opinion/signin.html', {'form':form, 'm':'Invalid Login Details'}) 
								
	else:
		form=AuthenticationForm()
		return  render(request,'opinion/signin.html', {'form':form})		
		
	
def logout_view(request):
	#logout(request)
	return  render(request,'opinion/logout.html')
