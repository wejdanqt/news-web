from django.views.generic import CreateView
from .forms import RegistrationForm
from django.urls import reverse_lazy

# Create your views here.


class SignUpFormView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'
