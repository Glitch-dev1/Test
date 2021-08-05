from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from decorators import unauth_only
from products.models import Product
from .forms import NewUserForm

def home_page(request):
    
    context = {
        "product": Product
    }
    return render(request, 'base.html', context)

@unauth_only
def register_request(request):
  form = NewUserForm()
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      group = Group.objects.get(name= "users")
      user.groups.add(group)
      return redirect("/login/")
      messages.success(request, "Account has been successfully created")
    
    
  context = {"form" : form}
  return render(request, "register.html", context)

@unauth_only
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, 'login.html',{})

def logout_req(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/login/")
  
def create_product(request):
    
    context = {
        
    }
    return render(request, 'create.html', context)
    
    
    