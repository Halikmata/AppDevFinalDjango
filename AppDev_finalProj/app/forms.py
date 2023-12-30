from django.forms import ModelForm
from django import forms
from .models import Guardians, Teachers, Students

class GuardiansForm(ModelForm):
    class Meta:
        model = Guardians
        fields = "__all__"
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
        }

class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'admission_date': forms.DateInput(attrs={'type': 'date'}),
        }

class TeachersForm(ModelForm):
    class Meta:
        model = Teachers
        fields = "__all__"
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
        }
