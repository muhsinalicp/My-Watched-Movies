from django.forms import ModelForm
from django import forms
from . models import Movie_info , CensorInfo

class MovieForm(ModelForm):
    class Meta:
        model = Movie_info
        fields = ["title" , "year" , "summary" , "image"]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter movie title',
                'class': 'form-input',
            }),
            'year': forms.NumberInput(attrs={
                'placeholder': 'Year',
                'class': 'form-input',
            }),
            'summary': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Brief summary',
                'class': 'form-input',
            }),
        }

class CensorForm(ModelForm):
    class Meta:
        model = CensorInfo
        fields = "__all__"
        widgets = {
            'rating': forms.TextInput(attrs={'placeholder': 'Rating'}),
            'certified_by': forms.TextInput(attrs={'placeholder': 'Certified by'}),
        }