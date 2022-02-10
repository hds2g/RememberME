from django.views import View
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, reverse
from django.views.generic import FormView, DetailView, UpdateView
from django.http import HttpResponse
from .models import User
from remembers import models as remember_models


class UserProfileView(DetailView):

    """UserProfileView Definition"""

    model = User
    # context_object_name = "user_obj"
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        tag_set = set()
        stage_list = list()
        stage_remember_number = list()

        user = User.objects.get(pk=pk)

        for s in remember_models.Remember.REMEMBER_STAGE:  #
            # print(s[1])
            stage_list.append(s[1])

            stage_remember_number.append(user.remembers.filter(stage=s[0]).count())
            # print(remember.stage, s[0], type(s))
            # update_idx = Remember.REMEMBER_STAGE.index(s) + 1

        # print(context)
        for remember in user.remembers.all():
            # if not remember.tags.all():
            #    print("None")
            # else:
            # remembers = Remember.objects.filter(user=user, stage=stage_days)
            # print(remembers.count())
            for tag in remember.tags.all():
                # print(tag)
                tag_set.add(tag)
        # context["common_tags"] = User.remembers.tags.most_common()[:4]
        # print(tag_set)
        # print(stage_list)
        # print(remembers.values("tags"))
        context["tags"] = tag_set
        context["stages"] = zip(stage_list, stage_remember_number)
        # context["stages_remember_number"] = stage_remember_number
        return context


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
