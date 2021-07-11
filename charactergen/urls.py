from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_random_character/', views.get_random_character, name='get_random_character'),
]
