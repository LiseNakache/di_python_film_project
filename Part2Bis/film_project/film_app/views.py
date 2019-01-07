from django.shortcuts import render, redirect
from film_app.models import Producer,Film,Category,Country,Poster
from film_app.forms import AddPosterForm, AddProducerForm, AddFilmForm,EditProducerForm, EditFilmForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def homepage(request):
    films = Film.objects.all().order_by('id')
    return render(request, 'homepage.html', {'films':films})

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

    return render(request, 'producer/addProducer.html', context={'add_producer_form': AddProducerForm()})

def addFilm(request):
    if request.method == 'POST':
        # /////Film////////////
        # title = request.POST.get('title')
        # release_date = request.POST.get('release_date')
        # categoryId = request.POST.get('category')
        # countryId = request.POST.get('country')
        # category = Category.objects.get(id=categoryId)
        # country = Country.objects.get(id=countryId)


        # /////Poster////////////
        # image = request.FILES['image']
        # explanation_text = request.POST.get('explanation_text')
        # print(image.name)
        # print(image.size)
        # poster = Poster.objects.get_or_create(image= image, explanation_text=explanation_text)
        #
        # Film.objects.get_or_create(title=title, release_date=release_date, category=category, country=country,poster=poster)
        # Pose pb : erreur, comment ajouter une image en même temps que le film ?



        # ////Autre Méthode////
        add_poster_form = AddPosterForm(request.POST, request.FILES)
        add_film_form = AddFilmForm(request.POST)

        poster = add_poster_form.save()
        film = add_film_form.save(False)
        film.poster = poster
        film.save()


        response = "Film ajouté"
    else:
        response = "Veuillez ajouter un film"

    return render(request, 'film/addFilm.html', context={
        'add_film_form': AddFilmForm(),
        'add_poster_form': AddPosterForm(),
        'response': response
    })


def editProducer(request, producer_id):
    producer = Producer.objects.get(id=producer_id)

    if request.method == 'POST':
        producer.first_name = request.POST.get('first_name')
        producer.last_name = request.POST.get('last_name')
        producer.save()

        response = "Réalisateur modifié"
        return redirect('/film_app/homepage/')
    else:
        response = "Veuillez modifier le réalisateur"

    producer_data = {
        'first_name': producer.first_name,
        'last_name': producer.last_name,
    }

    edit_producer_form = EditProducerForm(initial=producer_data)

    return render(request, 'producer/editProducer.html', context={'edit_producer_form': edit_producer_form})


def editFilm(request, film_id):
    film = Film.objects.get(id=film_id)

    if request.method == 'POST':
        film.title = request.POST.get('title')
        film.release_date = request.POST.get('release_date')
        categoryId = request.POST.get('category')
        countryId = request.POST.get('country')
        film.category = Category.objects.get(id=categoryId)
        film.country = Country.objects.get(id=countryId)
        film.save()

        response = "Film modifié"
        return redirect('/film_app/homepage/')
    else:
        response = "Veuillez modifier le film"

    film_data = {
        'title': film.title,
        'release_date': film.release_date,
        'category': film.category,
        'country' : film.country
    }

    edit_film_form = EditFilmForm(initial=film_data)

    return render(request, 'film/editFilm.html', context={'edit_film_form': edit_film_form})


