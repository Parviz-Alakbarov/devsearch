from .models import Profile, Skill
from django.db.models import Q


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
