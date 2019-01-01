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

class EditProducerForm(forms.ModelForm):
  class Meta:
    model   = Producer
    fields  = ['first_name', 'last_name']


class EditFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
