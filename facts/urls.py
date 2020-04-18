from django.urls import path
from . import views

urlpatterns = [
    path('random-fact', views.random, name='random'),
    path('viewall', views.viewall, name='viewall')
]
