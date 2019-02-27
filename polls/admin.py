from django.contrib import admin

# Register your models here.
from .models import Recipe, Exercise

admin.site.register(Recipe)
admin.site.register(Exercise)