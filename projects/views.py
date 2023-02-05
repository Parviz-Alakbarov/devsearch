from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Porject
from .forms import ProjectForm


def projects(request):
    projectList = Porject.objects.all()

    return render(request, 'projects/projects.html', {'projects': projectList})


def project(request, name):
    projectObj = Porject.objects.get(id=name)
    tags = projectObj.tags.all()
    return render(request, 'projects/project.html', {'project': projectObj, 'tags': tags})


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, 'projects/project_form.html', {'form': form})


def updateProject(request, pk):
    project = Porject.objects.get(id=pk)

    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, 'projects/project_form.html', {'form': form})


def deleteProject(request, pk):
    project = Porject.objects.get(id=pk)
    if request.method == 'POST':
        project.delete();
        return redirect('projects')
    return render(request, 'projects/delete_template.html', {'object':project})