from django.urls import path
from . import views

app_name = "all"
urlpatterns = [
    path('', views.home, name="home"),
    path('projects/<str:owner>/<str:repo_name>/doc/', views.project_documentation_view, name='project_doc'),
]