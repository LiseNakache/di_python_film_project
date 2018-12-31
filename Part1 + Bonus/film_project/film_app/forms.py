from django import forms
from film_app.models import Producer, Film


class AddProducerForm(forms.ModelForm):
  class Meta:
    model   = Producer
    fields  = '__all__'


class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
