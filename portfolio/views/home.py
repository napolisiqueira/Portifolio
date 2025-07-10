from django.shortcuts import render
from portfolio.models import Article, Project

def home(request):
    #Aqui tenho que que pegar os ultimos tres artigos e pegar os projetos.
    articles = Article.objects.all().order_by('-created_at')[:3]
    projects = Project.objects.all()
    context = {
        'articles': articles,
        'projects': projects,
    }

    return render(request, 'home.html', context)