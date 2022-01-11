from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Member


# Create your views here.
class HomepageView(ListView):
    model = Member
    template_name_suffix = '_homepage'

class MemberListView(ListView):
    model = Member

class MemberCreateView(CreateView):
    model = Member
    fields = ['member_name','member_info']
    template_name_suffix = '_create'
    success_url = reverse_lazy('list')


class MemberDetailView(DetailView):
    model = Member

class MemberUpdateView(UpdateView):
    model = Member
    fields = ['member_name','member_info']
    template_name_suffix = '_update'
    success_url = reverse_lazy('list')

class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('list')
    template_name_suffix = '_delete'


