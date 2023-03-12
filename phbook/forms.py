from django import forms

from . import models


class CreatePerson(forms.ModelForm):
    phones = forms.CharField(widget=forms.Textarea(), help_text="separated by new line '\n'")
    class Meta:
        model = models.Person
        fields = {
            'name',
            'phones'

        }

