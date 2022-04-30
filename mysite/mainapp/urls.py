from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_room', views.create_room, name='create_room'),
    path('lobby', views.lobby, name='lobby'),
    path('join_room',views.join_room, name='join_room'),
    path('wordinput',views.wordinput, name='wordinput'),
    path('game', views.game, name='game')
]