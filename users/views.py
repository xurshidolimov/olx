from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'profile_update.html'
    fields = ['username', 'email', 'phone_number']
    success_url = reverse_lazy('home')