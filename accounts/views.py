from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin

from .forms import CustomUserCreationForm
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    success_message = "Your account has been created successfully!"
    
User = get_user_model()

class ProfileView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('profile')
    success_message = "Your profile has been updated successfully!"

    def get_object(self):
        return self.request.user