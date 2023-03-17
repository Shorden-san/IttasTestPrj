from django import forms

from . import models


class CreatePerson(forms.ModelForm):
    phones = forms.CharField()
    class Meta:
        model = models.Person
        fields = {
            'name',
            'phones'
        }

