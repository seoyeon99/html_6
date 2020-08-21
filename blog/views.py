from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.contrib import auth




# Create your views here.

def index(request):
    return render(
        request,
        'blog/index.html'
    )
