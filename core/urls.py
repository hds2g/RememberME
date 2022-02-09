from django.urls import path
from remembers import views as remember_views
from remembers.views import (
    markdown_uploader,
)

app_name = "core"

urlpatterns = [
    path("", remember_views.HomeView.as_view(), name="home"),
    path("api/uploader/", markdown_uploader, name="markdown_uploader_page"),
]
