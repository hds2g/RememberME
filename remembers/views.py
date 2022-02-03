from datetime import date
from datetime import datetime, timedelta
from django.conf import settings
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    View,
    UpdateView,
    FormView,
)
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.forms import ModelForm
from .forms import RememberForm

from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt
from django.core.exceptions import BadRequest
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from .models import Remember

# from users import models


class HomeView(ListView):
    """HomeView Definition"""

    model = Remember

    paginate_by = 5
    paginate_orphans = 2
    # ordering = "created"
    context_object_name = "remembers"
    template_name = "remembers/remember_list.html"
    # print(model)

    def get_queryset(self):
        # print(self.request.user)
        # user_remember = models.Remember.objects.get(user=self.request.user)
        # print(user_remember)
        # print(self.request.user.is_anonymous)
        if self.request.user.is_authenticated:
            # return models.Remember.objects.filter(user=self.request.user)

            return Remember.objects.filter(user=self.request.user).exclude(
                showing_date__gt=date.today()
            )
        else:
            return []

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["common_tags"] = Remember.tags.most_common()[:4]

        # print(remembers.values("tags"))

        return context


@login_required
def delete(request, id):
    instance = get_object_or_404(Remember, id=id)

    # Remember.objects.filter(id=id).delete()
    instance.delete()
    return redirect("core:home")


@login_required
def edit(request, id):
    instance = get_object_or_404(Remember, id=id)

    form = RememberForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect("/remembers/{}/".format(instance.id))
    return render(request, "remembers/edit.html", {"form": form})


@login_required
def detail(request, id):
    # print(request.user)
    # remember = Remember.objects.filter(user=request.user, id=id)
    remember = Remember.objects.filter(user=request.user).get(id=id)
    # print(id)
    print(remember.tags)
    return render(request, "remembers/detail.html", {"remember": remember})


@csrf_exempt
def remember_ok(request, id):
    user = request.user
    # get remember.
    remember = Remember.objects.get(pk=id)

    if user == remember.user:

        for s in Remember.REMEMBER_STAGE:  #
            if remember.stage == s[0]:
                print(remember.stage, s[0], type(s))
                update_idx = Remember.REMEMBER_STAGE.index(s) + 1

                # if already max stage, just let it be
                if update_idx >= len(Remember.REMEMBER_STAGE):
                    break

                remember.stage = Remember.REMEMBER_STAGE[update_idx][0]
                # print(remember.stage)

                break
        # Update showing_date
        for s in Remember.REMEMBER_STAGE:
            if remember.stage == s[0]:
                print(f"updated showing date : {remember.stage}")
                remember.showing_date = datetime.today() + timedelta(
                    days=int(remember.stage)
                )

        remember.save()

        return HttpResponse("ok :)")

    else:
        # bad request
        return BadRequest("Invalid request.")


@csrf_exempt
def remember_ng(request, id):
    user = request.user
    # get remember.
    remember = Remember.objects.get(pk=id)

    if user == remember.user:
        remember.stage = Remember.STAGE_1WEEK
        remember.showing_date = datetime.today() + timedelta(days=7)

        remember.save()

        return HttpResponse("ok :)")

    else:
        # bad request
        return BadRequest("Invalid request.")


class AllView(ListView):
    """AllView Definition"""

    model = Remember

    paginate_by = 5
    paginate_orphans = 2
    ordering = "created"
    context_object_name = "remembers"
    template_name = "remembers/remember_list.html"
    print("AllView")
    # theme = getattr(settings, "MARTOR_THEME", "bootstrap")
    # return render(request, '%s/test_markdownify.html' % theme, context)
    # template_name = "%s/test_markdownify.html" % theme
    # print(template_name)
    # print(model)

    def get_queryset(self):
        # print(self.request.user)
        # user_remember = Remember.objects.get(user=self.request.user)
        # print(user_remember)
        # print(self.request.user.is_anonymous)
        if self.request.user.is_authenticated:
            # return Remember.objects.filter(user=self.request.user)

            # print(Remember.objects.filter(user=self.request.user).order_by("-created"))
            return Remember.objects.filter(user=self.request.user).order_by("-created")
        else:
            return []

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["common_tags"] = Remember.tags.most_common()[:4]
        return context


def tagged(request, slug):
    print(slug)
    tag = get_object_or_404(Tag, slug=slug)
    print(tag)
    # print(type(slug))
    print(type(tag))
    # Filter posts by tag name
    if request.user.is_authenticated:
        common_tags = Remember.tags.most_common()[:4]
        # print(common_tags)
        # Fix ME: filter tags=tag has error on django 4.0
        # so, I downgrage django to 3.2
        remembers = Remember.objects.filter(user=request.user, tags=tag).exclude(
            showing_date__gt=date.today()
        )

    else:
        return []

    print(remembers)
    context = {
        "tag": tag,
        "common_tags": common_tags,
        "remembers": remembers,
    }

    # FIX ME: need to change template for tagged
    return render(request, "remembers/remember_list.html", context)


@login_required
def add(request):
    user = request.user

    common_tags = Remember.tags.most_common()[:4]
    if request.method == "POST":
        form = RememberForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            remember = form.save(commit=False)
            remember.user = user
            remember.save()
            form.save_m2m()
            return redirect("core:home")
        else:
            # form = RememberForm()  # by this remove : "This field is required."
            print(form.errors.as_data())
    else:  # GET
        form = RememberForm()

    context = {
        "common_tags": common_tags,
        "form": form,
    }
    return render(request, "remembers/add.html", context)
