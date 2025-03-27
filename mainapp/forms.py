from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше ім'я")
    subject = forms.CharField(max_length=100, label="Тема")
    email = forms.EmailField(label="Ваш email")
    message = forms.CharField(widget=forms.Textarea, label="Повідомлення")