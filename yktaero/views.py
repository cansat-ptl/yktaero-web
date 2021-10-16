from django.db.models.fields import SlugField
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.html import escape
from ratelimit.decorators import ratelimit
from .models import Post, Tag, Project, Item, Feedback

# Function based views for static html pages


def news(request):
    return render(request, 'yktaero/news.html')


def contacts(request):
    return render(request, 'yktaero/about/contacts.html')


def staff(request):
    return render(request, 'yktaero/about/staff.html')


def partners(request):
    return render(request, 'yktaero/about/partners.html')


@ratelimit(key='ip', rate='10/m', block=True)
@csrf_protect
def feedback(request):
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        email = request.POST.get('email', 'invalid')
        try:
            validate_email(request.POST.get('email', 'invalid'))
        except ValidationError:
            messages.error(
                request, "Недопустимый формат электронной почты. Пожалуйста, проверьте правильность введённых данных и попробуйте ещё раз.")
            return HttpResponseRedirect(next)

        name = escape(request.POST.get('firstname', 'invalid'))
        subj = escape(request.POST.get('subject', 'invalid')[:3000])

        fb = Feedback.objects.create(name=name, email=email, text=subj)
        fb.save()

        messages.success(request, "Спасибо, ваша заявка принята. Ожидайте ответа на почту " +
                         email + " в течение 3-5 рабочих дней.")
        return HttpResponseRedirect(next)

# Class-based views for django-distill blog


class IndexView(ListView):

    template_name = 'yktaero/index.html'
    model = Post
    allow_empty = True
    queryset = Post.objects.published()[:3]
    ordering = None
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.queryset = Post.objects.published()[:3]
        return context


class NewsView(ListView):

    paginate_by = 10
    template_name = 'yktaero/news.html'
    model = Post, Tag
    allow_empty = True
    queryset = Post.objects.published()
    ordering = None
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        self.queryset = Post.objects.published()
        context['alltags'] = Tag.objects.all()
        return context


class PostView(DetailView):

    template_name = 'yktaero/post.html'
    model = Post


class ItemView(DetailView):

    template_name = 'yktaero/item.html'
    model = Item


class TagView(DetailView):

    paginate_by = 10
    template_name = 'yktaero/tag.html'
    model = Tag
    allow_empty = True
    ordering = None
    slug_field = 'name'
    slug_url_kwarg = 'tag'
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        self.queryset = self.model.post_set
        context['alltags'] = Tag.objects.all()
        return context


class ProjectView(DetailView):

    template_name = 'yktaero/project.html'
    model = Project
    allow_empty = True
    slug_field = 'name'
