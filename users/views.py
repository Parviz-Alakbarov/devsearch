from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Profile
from .forms import  CustomUserCreationForm


def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles': profiles})


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    skills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    projects = profile.porject_set.all()
    return render(request, 'users/user-profile.html',
                  {'profile': profile, 'skills': skills, 'otherSkills': otherSkills, 'projects': projects})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'UserName does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or Password is incorrect')

    return render(request, 'users/login_register.html', {'page': 'login'})


def logoutUser(request):
    logout(request)
    messages.info(request, "User has been logouted")
    return redirect('login')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User have been created successfully')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An error has occurred during registration')
    return render(request, 'users/login_register.html', {'page': 'register', 'form': form})
