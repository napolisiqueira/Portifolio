import requests
from django.shortcuts import render
import markdown
from django.conf import settings

def project_documentation_view(request, owner, repo_name):
    github_api_url = f"https://api.github.com/repos/{owner}/{repo_name}/readme"

    headers = {
        "Accept": "application/vnd.github.v3.raw", 
        "Authorization": f"token {settings.GITHUB_TOKEN}",
    }

    try:
        response = requests.get(github_api_url, headers=headers)
        response.raise_for_status() 

        readme_content_html = response.text

        context = {
            'readme_html': readme_content_html,
            'project_name': repo_name.replace('-', ' ').title(),
        }
        return render(request, 'global/project.html', context)

    except requests.exceptions.RequestException as e:
        context = {
            'error_message': f"Não foi possível carregar a documentação do projeto: {e}",
            'project_name': repo_name.replace('-', ' ').title(),
        }
        return render(request, 'global/project.html', context, status=500) # Renderiza uma página de erro