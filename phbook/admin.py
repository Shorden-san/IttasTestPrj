from django.contrib import admin

# Register your models here.

from .models import Person, Phone


admin.site.register(Person)
admin.site.register(Phone)