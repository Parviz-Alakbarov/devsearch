from django.shortcuts import render
from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles': profiles})


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    skills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    projects = profile.porject_set.all()
    return render(request, 'users/user-profile.html',
                  {'profile': profile, 'skills': skills, 'otherSkills': otherSkills, 'projects':projects})
