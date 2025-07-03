from django.urls import path
from . import views

app_name = "all"
urlpatterns = [
    path('', views.home, name="home"),
]