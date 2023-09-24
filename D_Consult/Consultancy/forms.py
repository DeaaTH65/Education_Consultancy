from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    subject = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject'}))
    message = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'}))
    
    
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']
