from .models import Porject, Tag
from django.db.models import Q


def searchProjects(request):
    search_text = ''
    if request.GET.get('search_query'):
        search_text = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_text)

    projectList = Porject.objects.distinct().filter(
        Q(title__icontains=search_text) |
        Q(description__icontains=search_text) |
        Q(owner__name__icontains=search_text) |
        Q(tags__in=tags)
    )
    return projectList, search_text