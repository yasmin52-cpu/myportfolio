from django.urls import path
from main.views import (
    show_main,
    show_experience,
    show_project,
    create_project,
    update_project,
    delete_project,
    show_json_projects,
    show_art,
    send_message,
    get_messages_json,
    delete_message,
    show_json_projects)
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('experience/', show_experience, name='show_experience'),
    path('projects/', show_project, name='show_project'),
    path('projects/add/', create_project, name='create_project'),
    path('projects/edit/<int:id>/', update_project, name='update_project'),
    path('projects/delete/<int:id>/', delete_project, name='delete_project'),
    path('projects/json/', show_json_projects, name='show_json_projects'),
    path('art/', show_art, name='show_art'),
    path('pesan/', send_message, name='send_message'),
    path("api/messages/", get_messages_json, name="get_messages_json"),
    path("pesan/<int:message_id>/delete/", delete_message, name="delete_message"),
]