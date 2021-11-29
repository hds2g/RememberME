from django.urls import path
from remembers import views as remember_views


app_name = "core"

urlpatterns = [path("", remember_views.HomeView.as_view(), name="home")]
