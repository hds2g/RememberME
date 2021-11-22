from django.urls import path
from remembers.views import postdetail, uploadi, uploadf, upload_link_view
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = "remembers"

urlpatterns = [
    path("<int:pk>/", postdetail, name="detail"),
    path("uploadi/", csrf_exempt(uploadi), name="uploadi"),
    path("uploadf/", csrf_exempt(uploadf), name="uploadf"),
    path("linkfetching/", upload_link_view, name="linkfetching"),
]
