from django.shortcuts import render,redirect
from django.contrib.auth import *
# Create your views here.

def logout_view(request):
	logout(request)
	return redirect('/')
