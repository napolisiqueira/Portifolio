from django.shortcuts import render
from portfolio.models import Article

def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})