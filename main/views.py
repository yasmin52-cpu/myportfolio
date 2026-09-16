from django.shortcuts import render, redirect
from .models import Experience, Education, Project, ArtItem
from django.contrib import messages
from .forms import MessageForm
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