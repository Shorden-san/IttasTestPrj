from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from . import forms, models


# Create your views here.
class home_page(TemplateView):
    template_name = 'phbook/home_page.html'  # выбор шаблона отрисовки

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['person'] = models.Person.objects.all()
        return context


class AddPhoneView(CreateView):
    template_name = 'phbook/create_person.html'
    form_class = forms.CreatePerson
    success_url = reverse_lazy('home')

    def get_success_url(self) -> str:
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            models.Phone.objects.create(number=phone_number, person_id=self.object)
            # models.Person.objects.create(name=self.object)
        return super().get_success_url()