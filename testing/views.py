from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login as auth_login,logout
# Create your views here.
from django.contrib import messages
from django.http import HttpResponse
from .models import movie
def homepage(request):
    m = movie.objects.all()
    return render(request,'index.html',{'movie':m})