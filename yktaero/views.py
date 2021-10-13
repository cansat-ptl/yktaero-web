from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Tag

# Function based views for static html pages

def index(request):
    posts = []
    return render(request, 'yktaero/index.html', {'posts': posts})


def news(request):
    return render(request, 'yktaero/news.html')


def contacts(request):
    return render(request, 'yktaero/about/contacts.html')


def staff(request):
    return render(request, 'yktaero/about/staff.html')


def partners(request):
    return render(request, 'yktaero/about/partners.html')


def payloads(request):
    return render(request, 'yktaero/projects/payloads.html')


def yktsat(request):
    return render(request, 'yktaero/projects/yktsat.html')


def rockets(request):
    return render(request, 'yktaero/projects/sounding-rockets.html')


def ground(request):
    return render(request, 'yktaero/projects/ground-equipment.html')

# Class-based views for django-distill blog

class IndexView(ListView):

    paginate_by = 3
    template_name = 'yktaero/index.html'
    model = Post
    allow_empty = True
    queryset = Post.objects.latest()
    ordering = '-created'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        NewsView.queryset = Post.objects.latest()
        return context


class NewsView(ListView):

    paginate_by = 10
    template_name = 'yktaero/news.html'
    model = Post
    allow_empty = True
    queryset = Post.objects.published()
    ordering = '-created'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        NewsView.queryset = Post.objects.published()
        return context


class PostView(DetailView):

    template_name = 'yktaero/post.html'
    model = Post


class TagView(DetailView):

    template_name = 'yktaero/tag.html'
    model = Tag
    slug_url_kwarg = 'tag'
    slug_field = 'name'