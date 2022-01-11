from django.urls import path
from .views import *

urlpatterns=[
    path('list/',BlogListView.as_view(), name='blog_list'),
    path('add/',BlogCreateView.as_view(), name='blog_add'),
    path('detail/<int:pk>/',BlogDetailView.as_view(),name='blog_detail'),
    path('update/<int:pk>',BlogUpdateView.as_view(),name='blog_update'),
    path('delete/<int:pk>',BlogDeleteView.as_view(),name='blog_delete'),
]