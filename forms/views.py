from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.
# request -> response (a view function takes a request and returns a response)
# request handler


title = ['title1', 'title2']


def form1(request):
    return HttpResponse('forms1')


def hello(request):
    context = {
        'posts': Post.objects.all(),
        'title': title[1],
    }
    return render(request, 'home.html', context)


class PostListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "postform.html"
    fields = ['title', 'content']

    def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)
