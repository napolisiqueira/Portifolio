from django.shortcuts import render
from portfolio.models import Article

def articles_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return render(request, 'portfolio/404.html', status=404)

    return render(request, 'articles_detail_page.html', {'article': article})