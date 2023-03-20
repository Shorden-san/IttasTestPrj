from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from . import forms, models
from .models import Phone, Person


class home_page(TemplateView):
    template_name = 'phbook/home_page.html'

    # def main_page(self, request):
    #     person = models.Person.objects.filter(user=request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_by = self.request.GET.get('search_by')
        search_info = self.request.GET.get('search_info')
        search_message = "All phones"
        if search_by in ['phone', 'name'] and search_info:
            if search_by == 'name':
                person = models.Person.objects.filter(name=search_info)
            else:
                person = models.Person.objects.filter(
                    phones__number__startswith=search_info)
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

    def get_user(request):
        current_user = request.user
        current_user_id = current_user.id
        print (current_user_id)

    # def get_success_url(self) -> str:
    #     phone_numbers = self.request.POST.get('phones')
    #     for phone_number in phone_numbers.split('\n'):
    #         models.Phone.objects.create(number=phone_number, person_id=self.object)
    #     return super().get_success_url()

    def get_success_url(self, request) -> str:
        phone_numbers = self.request.POST.get('phones')
        current_user = request.user
        current_user_id = current_user.id
        for phone_number in phone_numbers.split('\n'):
            models.Phone.objects.create(number=phone_number, person_id=self.object)
            models.Person.objects.create(user=current_user_id)
        return super().get_success_url()

class DeletePhoneView(DeleteView):
    model = models.Person
    template_name = 'phbook/delete_person.html'
    success_url = reverse_lazy('home')


class UpdatePhoneView(UpdateView):
    model = Phone
    fields = ['number']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('home')
