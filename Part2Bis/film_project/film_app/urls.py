from django.urls import path
from . import views

app_name = 'film_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('addProducer/', views.addProducer, name='addProducer'),
    path('addFilm/', views.addFilm, name='addFilm'),
    path('editFilm/<int:film_id>', views.editFilm, name='editFilm'),
    path('editProducer/<int:producer_id>', views.editProducer, name='editProducer'),
]
