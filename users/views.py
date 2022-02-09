from django.views import View
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, reverse
from django.views.generic import FormView, DetailView, UpdateView
from django.http import HttpResponse
from . import models


class UserProfileView(DetailView):

    """UserProfileView Definition"""

    model = models.User
    context_object_name = "user_obj"


class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")


def log_out(request):
    # messages.info(request, "See you later")
    logout(request)
    return redirect(reverse("core:home"))


def email_success(request):
    res = "Email is verified!"
    # return HttpResponse("<p>%s</p>" % res)
    return redirect(reverse("core:home"))
