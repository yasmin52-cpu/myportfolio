import datetime
from django.shortcuts import render, redirect
from main.models import Message
from .models import Experience, Education, Project, ArtItem
from .forms import MessageForm, ProjectForm, ExperienceForm
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.core import serializers
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

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
        'education_list': Education.objects.all(),
        'is_editor': is_editor,
        'form': ExperienceForm(),
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
@require_POST
def delete_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=id)
    experience.delete()
    return redirect('main:show_experience')

def show_json_experiences(request):
    """Endpoint GET JSON untuk daftar Experience (AJAX load + search).

    JSON dibuat manual agar field turunan (star_count, has_starred) ikut terkirim.
    Aman untuk guest: has_starred selalu False jika user belum login.
    """
    query = request.GET.get("q", "").strip()
    experiences = Experience.objects.prefetch_related('starred_by')
    if query:
        experiences = experiences.filter(
            Q(title__icontains=query) | Q(organization__icontains=query)
        )

    # Menghitung dari hasil prefetch (len) agar tidak ada query tambahan per item (N+1).
    current_user_id = request.user.id if request.user.is_authenticated else None
    data = []
    for exp in experiences:
        starred_users = list(exp.starred_by.all())
        data.append({
            'pk': exp.id,
            'fields': {
                'title': exp.title,
                'organization': exp.organization,
                'description': exp.description,
                'category': exp.category,
                'category_display': exp.get_category_display(),
                'is_ongoing': exp.is_ongoing,
                'image_url': exp.image_url,
                'stars_count': len(starred_users),
                'has_starred': any(user.id == current_user_id for user in starred_users),
            }
        })

    return JsonResponse(data, safe=False)


@require_POST
def create_experience_ajax(request):
    """Menambah Experience via AJAX; selalu membalas JSON dengan status HTTP yang tepat.

    201 = berhasil, 400 = validasi ModelForm gagal, 403 = bukan superuser.
    Permission dicek di backend (bukan hanya menyembunyikan tombol di template),
    sehingga POST manual dari guest/user biasa tetap ditolak. 403 JSON dipakai
    (bukan redirect login) karena klien AJAX tidak bisa memproses redirect HTML.
    """
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Kamu tidak memiliki akses untuk menambahkan experience."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience berhasil ditambahkan.", "pk": experience.id},
            status=201,
        )
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

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
    title_query = request.GET.get("title", "").strip()
    
    is_admin = request.user.is_superuser
    is_editor = False
    
    if request.user.is_authenticated:
        is_editor = request.user.groups.filter(name='Editor').exists()

    context = {
        'title_query': title_query,
        'is_admin': is_admin,
        'is_editor': is_editor,
        'form': ProjectForm(), 
    }
    
    return render(request, 'project.html', context)

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

@login_required(login_url='/login/')
def update_project(request, id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied
        
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_project')
        
    context = {'form': form, 'title': 'Edit Project'}
    return render(request, 'message_form.html', context)

@login_required(login_url='/login/')
@require_POST
def delete_project(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    project = get_object_or_404(Project, pk=id)
    project.delete()
    return redirect('main:show_project')

def show_json_projects(request):
    title_query = request.GET.get("title", "").strip()
    
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "image_url": project.image_url,
                "play_url": project.play_url,
                
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)
    
@login_required(login_url="/login/")
def toggle_star_projects(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )
    
    # Form divalidasi menggunakan form yang sudah ada
    form = ProjectForm(request.POST)
    
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            # Ubah project.id yang bertipe UUID menjadi string
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )
        
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

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


@login_required(login_url='/login/')
def delete_message(request, message_id):
    if not request.user.is_superuser:
        raise PermissionDenied

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