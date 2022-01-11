from django.urls import path
from .views import *

urlpatterns=[
    path('',HomepageView.as_view(), name='homepage'),
    path('list/',MemberListView.as_view(), name='list'),
    path('add/',MemberCreateView.as_view(), name='add'),
    path('detail/<int:pk>/',MemberDetailView.as_view(),name='detail'),
    path('update/<int:pk>',MemberUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',MemberDeleteView.as_view(),name='delete'),
]