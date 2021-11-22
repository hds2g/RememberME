from django.shortcuts import render, redirect, get_object_or_404
from .models import Remember
from django.contrib import messages
from django.forms import ModelForm
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import requires_csrf_token

# Create your views here.


class RememberForm(ModelForm):
    class Meta:
        model = Remember
        fields = [
            "remember",
        ]


def home(request):
    if request.method == "POST":
        form = RememberForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, "submitted succesfully {}".format(post))
            return redirect("/")
    form = RememberForm()
    return render(request, "remembers/home.html", {"form": form})


def editpost(request, id):
    instance = get_object_or_404(Remember, id=id)
    form = RememberForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect("/{}/".format(instance.id))
    return render(request, "remembers/edit.html", {"form": form})


def postdetail(request, id):
    remember = Remember.objects.get(id=id)
    return render(request, "remembers/detail.html", {"remember": remember})


@requires_csrf_token
def uploadi(request):
    print(uploadi)
    f = request.FILES["image"]
    fs = FileSystemStorage()
    filename = str(f).split(".")[0]
    file = fs.save(filename, f)
    fileurl = fs.url(file)
    return JsonResponse({"success": 1, "file": {"url": fileurl}})


@requires_csrf_token
def uploadf(request):
    print(uploadf)
    f = request.FILES["file"]
    fs = FileSystemStorage()
    filename, ext = str(f).split(".")
    print(filename, ext)
    file = fs.save(str(f), f)
    fileurl = fs.url(file)
    fileSize = fs.size(file)
    return JsonResponse(
        {"success": 1, "file": {"url": fileurl, "name": str(f), "size": fileSize}}
    )


def upload_link_view(request):
    import requests
    from bs4 import BeautifulSoup

    print(request.GET["url"])
    url = request.GET["url"]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    metas = soup.find_all("meta")
    description = ""
    title = ""
    image = ""
    for meta in metas:
        if "property" in meta.attrs:
            if meta.attrs["property"] == "og:image":
                image = meta.attrs["content"]
        elif "name" in meta.attrs:
            if meta.attrs["name"] == "description":
                description = meta.attrs["content"]
            if meta.attrs["name"] == "title":
                title = meta.attrs["content"]
    return JsonResponse(
        {
            "success": 1,
            "meta": {
                "description": description,
                "title": title,
                "image": {"url": image},
            },
        }
    )
