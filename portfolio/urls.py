from django.urls import path
from django.urls import include

from . import views

app_name = 'portfolio'
urlpatterns = [
    path('articles/<int:article_id>', views.articles_detail, name='articles_detail'),
    path('projects/<int:project_id>', views.projects_details, name='projects_detail'),
    path('articles/', views.articles, name='articles'),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
]
