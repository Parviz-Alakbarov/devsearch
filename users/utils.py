from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def searchProfiles(request):
    search_text = ''

    if request.GET.get('search_query'):
        search_text = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_text)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_text) |
        Q(short_intro__icontains=search_text) |
        Q(skill__in=skills)
    )

    return profiles, search_text

def paginateProfiles(request, userList, results):
    page = request.GET.get('page')
    paginator = Paginator(userList, results)
    try:
        page = int(page)
        userList = paginator.page(page)
    except EmptyPage:
        if page > paginator.num_pages:
            page = paginator.num_pages
        else:
            page = 1
        userList = paginator.page(page)

    except (TypeError, PageNotAnInteger):
        page = 1
        userList = paginator.page(1)

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

    return custom_range, userList, paginator.num_pages
