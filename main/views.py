from django.shortcuts import render
from .models import Experience, Education, Project, ArtItem

def show_main(request):
    context = {
        'name': 'Yasmin',
        'npm': '2506606124',
        'study_program': 'Computer Science',
        'bio': 'Broke Computer Science Student Who Draws Sometimes.',
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        'experience_list': Experience.objects.all(),
        'education_list': Education.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    context = {
        'project_list': Project.objects.all(),
    }
    return render(request, "project.html", context)

def show_art(request):
    context = {
        'characters': ArtItem.objects.filter(category='characters'),
        'backgrounds': ArtItem.objects.filter(category='backgrounds'),
        'icons': ArtItem.objects.filter(category='icons'),
        'tilemaps': ArtItem.objects.filter(category='tilemaps'),
        'spritesheets': ArtItem.objects.filter(category='spritesheets'),
    }
    return render(request, "art.html", context)