from django.urls import path
from remembers.views import (
    detail,
    remember_ok,
    remember_ng,
    tagged,
    AllView,
    add,
    edit,
    delete,
)
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = "remembers"

urlpatterns = [
    path("<int:id>/", detail, name="detail"),
    path("<int:id>/ok/", remember_ok, name="ok"),
    path("<int:id>/ng/", remember_ng, name="ng"),
    path("all/", AllView.as_view(), name="all"),
    path("add/", add, name="add"),
    path("edit/<int:id>/", edit, name="edit"),
    path("delete/<int:id>/", delete, name="delete"),
    # Tag
    path("tag/<slug:slug>/", tagged, name="tagged"),
]
