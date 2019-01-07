from django import forms
from film_app.models import Producer, Film, Poster

class AddPosterForm(forms.ModelForm):
  class Meta:
    model   = Poster
    fields  = '__all__'

class AddProducerForm(forms.ModelForm):
  class Meta:
    model   = Producer
    fields  = '__all__'


class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        exclude = ['poster']

class EditProducerForm(forms.ModelForm):
  class Meta:
    model   = Producer
    fields  = ['first_name', 'last_name']


class EditFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
