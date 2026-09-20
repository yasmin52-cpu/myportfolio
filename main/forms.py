from django.forms import ModelForm, TextInput, Textarea, URLInput, RadioSelect, CheckboxInput
from main.models import Message, Project, Experience, ArtItem

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["sender", "content"]
        labels = {
            "sender": "Nama Kamu",
            "content": "Pesan",
        }
        widgets = {
            "sender": TextInput(attrs={"placeholder": "Masukkan nama...", "class": "form-control"}),
            "content": Textarea(attrs={"placeholder": "Ketik pesanmu di sini...", "rows": 4, "class": "form-control"}),
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [ "title", "description", "image_url", "play_url" ]
        labels = {
            "title" : "Title of your project",
            "description" : "Brief description of your project",
            "image_url" : "Url or path to your image",
            "play_url" : "Link to your project"
        }
        widgets = {
            "title": TextInput(attrs={"placeholder": "Masukkan judul project...", "class": "form-control"}),
            "description": Textarea(attrs={"placeholder": "Ketik deskripsi di sini...", "rows": 4, "class": "form-control"}),
            "image_url": TextInput(attrs={"placeholder": "https://...", "class": "form-control"}),
            "play_url": URLInput(attrs={"placeholder": "https://...", "class": "form-control"}),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "organization", "description", "category", "is_ongoing", "image_url"]
        
        labels = {
            "title": "Role / Position",
            "organization": "Organization / Company",
            "description": "Description",
            "category": "Category",
            "is_ongoing": "Ongoing",
            "image_url": "Image URL",
        }
        
        widgets = {
            "title": TextInput(attrs={"placeholder": "Contoh: Creative Manager", "class": "form-control"}),
            "organization": TextInput(attrs={"placeholder": "Contoh: Open House Fasilkom", "class": "form-control"}),
            "description": Textarea(attrs={"placeholder": "Jelaskan peran dan tugasmu...", "rows": 4, "class": "form-control"}),
            "category": RadioSelect(attrs={'class' : 'category-radio-group'}),
            "is_ongoing": CheckboxInput(attrs={'class': 'form-checkbox'}),
            "image_url": TextInput(attrs={"placeholder": "Contoh: https://drive.google.com/thumbnail?id=...&sz=w1000", "class": "form-control"}),
        }