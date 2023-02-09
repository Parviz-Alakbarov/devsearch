from .models import Porject, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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


def paginateProjects(request, projectList, results):
    page = request.GET.get('page')
    paginator = Paginator(projectList, results)
    try:
        page = int(page)
        projectList = paginator.page(page)
    except EmptyPage:
        if page > paginator.num_pages:
            page = paginator.num_pages
        else:
            page = 1
        projectList = paginator.page(page)

    except (TypeError, PageNotAnInteger):
        page = 1
        projectList = paginator.page(1)

    # leftIndex = page - 4
    # rightIndex = page + 5
    # if leftIndex < 1:
    #     leftIndex = 1
    #     rightIndex = rightIndex + 5
    #     if rightIndex>paginator.num_pages:
    #         rightIndex = paginator.num_pages
    # if rightIndex > paginator.num_pages:
    #     rightIndex = paginator.num_pages + 1
    #     leftIndex = leftIndex - 4
    #     if leftIndex <1:
    #         leftIndex = 1
    #
    # custom_range = range(leftIndex, rightIndex)

    page_range = paginator.page_range
    if paginator.num_pages > 10:
        if page <= 6:
            custom_range = page_range[:10]
        elif page > paginator.num_pages - 6:
            custom_range = page_range[-10:]
        else:
            custom_range = page_range[page - 6:page + 4]
    else:
        custom_range = page_range

    return custom_range, projectList, paginator.num_pages
