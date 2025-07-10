from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from portfolio.models import Article
from django.db.models import Q


def articles(request):
    articles_list = Article.objects.all()
    paginator = Paginator(articles_list, 10)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)


    return render(request, 'articles.html', {'articles': articles})
