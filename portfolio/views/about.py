from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os

def download_curriculo(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'docs', 'curriculo.pdf')
    
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    else:
        return render(request, '404.html') 
def about(request):
    return render(request, 'about_me.html')