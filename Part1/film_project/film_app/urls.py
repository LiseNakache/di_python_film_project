from django.urls import path
from . import views

app_name = 'film_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
]
