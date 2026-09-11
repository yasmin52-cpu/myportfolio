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
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    context = {
        'experience_list': experiences,
        'education_list': educations,
    }
    return render(request, "experience.html", context)

def show_projects(request):
    projects = Project.objects.all()
    context = {
        'project_list': projects,
    }
    return render(request, "project.html", context)

def show_art(request):
    art_items = ArtItem.objects.all()
    context = {
        'art_list': art_items,
        'characters': ArtItem.objects.filter(category='characters'),
        'backgrounds': ArtItem.objects.filter(category='backgrounds'),
        'icons': ArtItem.objects.filter(category='icons'),
        'tilemaps': ArtItem.objects.filter(category='tilemaps'),
        'spritesheets': ArtItem.objects.filter(category='spritesheets'),
    }
    return render(request, "art.html", context)