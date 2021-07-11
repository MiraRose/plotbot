from django.contrib import admin

# Register your models here.
from .models import Character, Genre

admin.site.register(Character)
admin.site.register(Genre)
