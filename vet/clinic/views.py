from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OwnerRegistrationForm, PetPatientCreateForm
from .models import PetPatient, Owner

class RegisterView(SuccessMessageMixin, CreateView):
    model = Owner
    form_class = OwnerRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('pet_add')
    success_message = "Регистрация прошла успешно! Теперь добавьте своего питомца."

    def form_valid(self, form):
        response = super().form_valid(form)
        from django.contrib.auth import login
        login(self.request, self.object)
        return response

class PetPatientCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = PetPatient
    form_class = PetPatientCreateForm
    template_name = 'petpatient_form.html'
    success_url = reverse_lazy('home')
    success_message = "Питомец успешно добавлен!"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = PetPatient.objects.filter(owner=self.request.user).order_by('name')
        return context