from django.contrib import admin

# Register your models here.
from .models import Country,Category,Film,Producer, Poster

admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Film)
admin.site.register(Producer)
admin.site.register(Poster)