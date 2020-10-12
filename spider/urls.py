from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('pages', views.pages, name='pages'),
]