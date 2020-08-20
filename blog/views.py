from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class PostList(ListView):
    model = Post
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        return context


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

def main(request):
    return render(request, 'main.html')

def base(request):
    return render(request, 'base.html')


class PostUpdate(UpdateView):
    model = Post
    fields = [
        'title', 'content', 'head_image', 'category', 'tags'
    ]


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)

        return context


class PostCreate(CreateView):
    model = Post
    fields = [
        'title', 'content', 'head_image',
    ]

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(type(self), self).form_valid(form)
        else:
            return redirect('/blog/')


# def post_detail(request, pk):
#     blog_post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'blog_post'= blog_post,
#         }
#     )

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
