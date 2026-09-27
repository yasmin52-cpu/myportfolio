import datetime
from django.shortcuts import render, redirect
from main.models import Message
from .models import Experience, Education, Project, ArtItem
from .forms import MessageForm, ProjectForm, ExperienceForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        'name': 'Yasmin',
        'npm': '2506606124',
        'study_program': 'Computer Science',
        'bio': 'Broke Computer Science Student Who Draws Sometimes.',
        "last_login" : last_login,
    }
    return render(request, "index.html", context)

# Experiences
def show_experience(request):
    is_editor = False
    if request.user.is_authenticated:
        is_editor = request.user.groups.filter(name='Editor').exists()
        
    context = {
        'experience_list': Experience.objects.all(),
        'education_list': Education.objects.all(),
        'is_editor': is_editor,
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
        
    context = {'form': form, 'title': 'Add New Experience'}
    return render(request, 'message_form.html', context)

@login_required(login_url="/login/")
def update_experience(request, id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=id)
    
    form = ExperienceForm(request.POST or None, instance=experience)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
        
    context = {'form': form, 'title': 'Edit Experience'}
    return render(request, 'message_form.html', context)

@login_required(login_url="/login/")
def delete_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=id)
    experience.delete()
    return redirect('main:show_experience')

def show_json_experiences(request):
    data = Experience.objects.all()
    return HttpResponse(
        serializers.serialize("json", data, use_natural_foreign_keys=True), 
        content_type="application/json"
    )
    
@login_required(login_url="/login/")
def toggle_star_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)
    return redirect("main:show_experience")

# Projects
def show_project(request):
    context = {
        'project_list': Project.objects.all(),
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ProjectForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_project')
    
    context = {'form': form, 'title': 'Add New Project'}
    return render(request, 'message_form.html', context)

def update_project(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_project')
        
    context = {'form': form, 'title': 'Edit Project'}
    return render(request, 'message_form.html', context)

def delete_project(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    project = get_object_or_404(Project, pk=id)
    project.delete()
    return redirect('main:show_project')

def show_json_projects(request):
    data = Project.objects.all()
    return HttpResponse(
        serializers.serialize("json", data, use_natural_foreign_keys=True), 
        content_type="application/json"
    )
    
@login_required(login_url="/login/")
def toggle_star_projects(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")

# Art Stuff
def show_art(request):
    context = {
        'characters': ArtItem.objects.filter(category='characters'),
        'backgrounds': ArtItem.objects.filter(category='backgrounds'),
        'icons': ArtItem.objects.filter(category='icons'),
        'tilemaps': ArtItem.objects.filter(category='tilemaps'),
        'spritesheets': ArtItem.objects.filter(category='spritesheets'),
    }
    return render(request, "art.html", context)

# Message
def send_message(request):
    form = MessageForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save() 
        messages.success(request, "Terima kasih! Pesanmu sudah terkirim.")
        return redirect("main:send_message") 

    json_response = get_messages_json(request)
    message_objects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    message_list = [msg.object for msg in message_objects]
    
    context = {
        "form": form,
        "message_list": message_list,
    }
    return render(request, "message_form.html", context)


def get_messages_json(request):
    sender_query = request.POST.get("sender", "").strip()
    messages = Message.objects.all()
    
    if sender_query:
        messages = messages.filter(sender__icontains=sender_query)
        
    messages_json = serializers.serialize("json", messages)
    return HttpResponse(messages_json, content_type="application/json")


def delete_message(request, message_id):
    message_item = get_object_or_404(Message, pk=message_id)
    if request.method == "POST":
        message_item.delete()
        messages.success(request, "Pesan berhasil dihapus!")
        return redirect("main:send_message")
    return redirect("main:send_message")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Yacchem",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response
    context = {
        "name": "Yacchem",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response