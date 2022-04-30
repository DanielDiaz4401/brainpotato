from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_room', views.create_room, name='create_room'),
]