from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Porject
from .forms import ProjectForm
from django.contrib import messages


def projects(request):
    projectList = Porject.objects.all()

    return render(request, 'projects/projects.html', {'projects': projectList})


def project(request, name):
    projectObj = Porject.objects.get(id=name)
    tags = projectObj.tags.all()
    return render(request, 'projects/project.html', {'project': projectObj, 'tags': tags})


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
        else:
            messages.error(request, 'An error has occurred during registration')
            print(form.errors)

    return render(request, 'projects/project_form.html', {'form': form})


@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if project is None:
        messages.error(request, "Project not found!")
        return redirect('projects')
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, 'projects/project_form.html', {'form': form})


@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile

    project = profile.porject_set.get(id=pk)
    if project is None:
        messages.error(request, 'Project not found')
        return redirect('projects')
    if request.method == 'POST':
        project.delete();
        return redirect('projects')
    return render(request, 'delete_template.html', {'object': project})
