from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
from portfolio.models import Certificados
import os

def download_curriculo(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'docs', 'curriculo.pdf')
    
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    else:
        return render(request, '404.html') 
    
def about(request):
    certificados = Certificados.objects.all()

    context = {
        'certificados': certificados
    }
    return render(request, 'about_me_page.html', context)