from django.urls import path

from . import views

urlpatterns = [
    path('covid19', views.covid, name='covid19'),
]