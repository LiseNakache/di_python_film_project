from django.shortcuts import render
# from film_app.models import Producer

# Create your views here.

def index(request):
    return render(request, 'index.html')


def homepage(request):
    return render(request, 'homepage.html')




