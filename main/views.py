from django.shortcuts import render
from main.models import Experience

def show_main(request):
    context = {
        "name": "Yasmin",
        "npm": "2506606124",
        "study_program": "S1 Ilmu Komputer",
        "bio": "Broke computer science student who draws sometimes",
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Yasmin",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)