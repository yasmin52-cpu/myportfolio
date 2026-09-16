from django.forms import ModelForm, TextInput, Textarea
from main.models import Message

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