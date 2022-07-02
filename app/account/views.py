from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView

from account.forms import UserCreateForm


class RegisterForm(FormView):
    form_class = UserCreateForm
    success_url = reverse_lazy('books')
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginForm(FormView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('books'))

