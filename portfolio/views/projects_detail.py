from django.shortcuts import render
from portfolio.models import Project

def projects_details(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return render(request, 'portfolio/404.html', status=404)

    return render(request, 'project_detail_page.html', {'project': project})