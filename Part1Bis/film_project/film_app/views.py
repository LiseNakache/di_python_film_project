from django.shortcuts import render
from film_app.models import Producer,Film,Category,Country
from film_app.forms import AddProducerForm, AddFilmForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def homepage(request):
    producers = Producer.objects.all().order_by('id')
    return render(request, 'homepage.html', {'producers':producers})




def addProducer(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        filmId = request.POST.get('film')
        film = Film.objects.get(id=filmId)

        Producer.objects.get_or_create(first_name=first_name, last_name=last_name, film=film)
        response = "Réalisateur ajouté"
    else:
        response = "Veuillez ajouter un realisateur"

    return render(request, 'addProducer.html', context={'add_producer_form': AddProducerForm()})

def addFilm(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        release_date = request.POST.get('release_date')
        categoryId = request.POST.get('category')
        countryId = request.POST.get('country')
        category = Category.objects.get(id=categoryId)
        country = Country.objects.get(id=countryId)

        Film.objects.get_or_create(title=title, release_date=release_date, category=category, country=country)
        response = "Film ajouté"
    else:
        response = "Veuillez ajouter un film"

    return render(request, 'addFilm.html', context={'add_film_form': AddFilmForm()})
