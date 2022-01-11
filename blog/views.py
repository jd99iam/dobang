from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Blog
# Create your views here.

class BlogListView(ListView):
    model = Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title','author','content']
    template_name_suffix = '_create'
    success_url = reverse_lazy('blog_list')


class BlogDetailView(DetailView):
    model = Blog

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title','author','content']
    template_name_suffix = '_update'
    success_url = reverse_lazy('blog_list')

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')
    template_name_suffix = '_delete'