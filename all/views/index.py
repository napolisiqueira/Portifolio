from django.shortcuts import render
from all.models import Article
# Create your views here.
def home(request):
    latest_articles = Article.objects.order_by('-created_it')[:3]   
    context = {
        "articles": latest_articles
    }

    return render(request, 'global/index.html',context)