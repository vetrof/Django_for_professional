from django.urls import reverse_lazy
from django.views import generic

from .admin import CustomUser
from .forms import CustomUserCreationForm



class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
