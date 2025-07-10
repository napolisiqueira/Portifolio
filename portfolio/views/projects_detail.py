from django.shortcuts import render
from portfolio.models import Project

def projects_details(request, projectid):
    try:
        project = Project.objects.get(id=projectid)
    except Project.DoesNotExist:
        return render(request, 'portfolio/404.html', status=404)

    return render(request, 'portfolio/projects_detail.html', {'project': project})