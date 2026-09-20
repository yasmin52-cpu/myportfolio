from django.shortcuts import render, redirect
from .models import Experience, Education, Project, ArtItem
from django.contrib import messages
from .forms import MessageForm, ProjectForm, ExperienceForm
from django.http import HttpResponse
from django.core import serializers
from main.models import Message
from django.shortcuts import get_object_or_404

def show_main(request):
    context = {
        'name': 'Yasmin',
        'npm': '2506606124',
        'study_program': 'Computer Science',
        'bio': 'Broke Computer Science Student Who Draws Sometimes.',
    }
    return render(request, "index.html", context)

# Experiences
def show_experience(request):
    context = {
        'experience_list': Experience.objects.all(),
        'education_list': Education.objects.all(),
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
        
    context = {'form': form, 'title': 'Add New Experience'}
    return render(request, 'message_form.html', context)

def update_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    
    form = ExperienceForm(request.POST or None, instance=experience)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
        
    context = {'form': form, 'title': 'Edit Experience'}
    return render(request, 'message_form.html', context)

def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    experience.delete()
    return redirect('main:show_experience')

def show_json_experiences(request):
    data = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Projects
def show_project(request):
    context = {
        'project_list': Project.objects.all(),
    }
    return render(request, "project.html", context)

def create_project(request):
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
    project = get_object_or_404(Project, pk=id)
    project.delete()
    return redirect('main:show_project')

def show_json_projects(request):
    data = Project.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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
    sender_query = request.GET.get("sender", "").strip()
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