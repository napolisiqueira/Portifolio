from django.shortcuts import render
from all.models import Article
# Create your views here.
def articles_focus(request, article_id):
    article = Article.objects.get(id=article_id)  

    context = {
        "articles": article
    }

    return render(request, 'global/article_blog.html', context)

def articles_blog(request):
    articles = Article.objects.all()

    context = {
        "articles": articles
    }

    return render(request, 'global/article.html',context)
