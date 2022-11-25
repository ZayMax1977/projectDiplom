from django import forms
from .models import *

class LawForm(forms.ModelForm):
    class Meta:
        model = Law
        fields = ['title','category', 'source','content','photo',"author"]
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'source': forms.TextInput(attrs={"class": "form-control",'placeholder':'www.sample.com'}),
            'content': forms.Textarea(attrs={"class": "form-control",'rows': 5}),
            'category': forms.Select(attrs={"class": "form-control",}),
            'author': forms.TextInput(attrs={"class": "form-control"}),

        }