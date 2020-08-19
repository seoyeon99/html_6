from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

def category_02_women(request):
    return render(request, 'category_02_women.html')

def category_01_economics(request):
    return render(request, 'category_01_economics.html')

def category_03_art(request):
    return render(request, 'category_03_art.html')

def category_04_humanities(request):
    return render(request, 'category_04_humanities.html')

def category_05_science(request):
    return render(request, 'category_05_science.html')







# Create your views here.

# def index(request):
#     posts = Post.objects.all()
#     return render(
#         request,
#         'blog/index.html',
#         {
#           'posts':posts,
#         }
#
#     )
