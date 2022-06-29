from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('home/<slug>', views.movie_detail, name='movie-detail'),

]
