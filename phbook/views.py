from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView
from . import forms, models


# Create your views here.
class home_page(TemplateView):
    template_name = 'phbook/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_by = self.request.GET.get('search_by')
        search_info = self.request.GET.get('search_info')
        search_message = "All phones"
        if search_by in ['phone', 'name'] and search_info:
            if search_by == 'name':
                person = models.Person.objects.filter(name=search_info)
            else:
                person = models.Person.objects.filter(phones__number__startswith=search_info) # лучше сделать строгую фильтрацию
            search_message = f"Sorted by {search_by}, element {search_info}"
            context['search_message'] = search_message
            context['person'] = person
            return context
        context['search_message'] = search_message
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


class DeletePhoneView(DeleteView):
    model = models.Person
    template_name = 'phbook/delete_person.html'
    success_url = reverse_lazy('home')