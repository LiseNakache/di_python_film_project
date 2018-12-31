from django.contrib import admin

# Register your models here.
from .models import Country,Category,Film,Producer

admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Film)
admin.site.register(Producer)
