from django.shortcuts import render

def custom_page_not_found_view(request, exception):

    response = render(request, '404.html', {}) # Passe qualquer contexto necessário
    response.status_code = 404
    return response