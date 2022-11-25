from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'name', 'phone', 'email', 'art', 'message']

        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'phone': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),

            'art': forms.TextInput(attrs={"class": "form-control",  'placeholder': 'Поле заполняется при жалобе на какое-либо объявление'}),
            'message': forms.Textarea(attrs={"class": "form-control", 'rows': 5 }),

        }