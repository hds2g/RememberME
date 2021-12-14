from django.urls import path
from remembers.views import (
    postdetail,
    uploadi,
    uploadf,
    upload_link_view,
    remember_ok,
    remember_ng,
    tagged,
    AllView,
)
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = "remembers"

urlpatterns = [
    path("<int:id>/", postdetail, name="detail"),
    path("<int:id>/ok/", remember_ok, name="ok"),
    path("<int:id>/ng/", remember_ng, name="ng"),
    path("all/", AllView.as_view(), name="all"),
    # EdiforJS
    path("uploadi/", csrf_exempt(uploadi), name="uploadi"),
    path("uploadf/", csrf_exempt(uploadf), name="uploadf"),
    path("linkfetching/", upload_link_view, name="linkfetching"),
    # Tag
    path("tag/<slug:slug>/", tagged, name="tagged"),
]
