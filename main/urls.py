from django.urls import path
from main.views import show_main, show_experience, show_projects, show_art, send_message, get_messages_json, delete_message

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('experience/', show_experience, name='show_experience'),
    path('projects/', show_projects, name='show_projects'),
    path('art/', show_art, name='show_art'),
    path('pesan/', send_message, name='send_message'),
    path("api/messages/", get_messages_json, name="get_messages_json"),
    path("pesan/<int:message_id>/delete/", delete_message, name="delete_message"),
]