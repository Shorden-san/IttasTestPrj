from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from . import forms, models


class home_page(TemplateView):
    template_name = 'phbook/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_by = self.request.GET.get('search_by')
        search_info = self.request.GET.get('search_info')
        search_message = "All phones"
        if search_by in ['number', 'name'] and search_info:
            if search_by == 'name':
                person = models.Person.objects.filter(name=search_info)
            else:
                person = models.Person.objects.filter(number=search_info)
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


class DeletePhoneView(DeleteView):
    model = models.Person
    template_name = 'phbook/delete_person.html'
    success_url = reverse_lazy('home')


class UpdatePhoneView(CreateView):
    template_name = 'phbook/update_person.html'
    form_class = forms.UpdatePerson
    success_url = reverse_lazy('home')