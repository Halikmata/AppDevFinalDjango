from django.forms import ModelForm
from django import forms
from .models import Guardian, Teacher, Student, Subject, Detention

class GuardiansForm(ModelForm):
    class Meta:
        model = Guardian
        fields = "__all__"
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
        }

class StudentsForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'admission_date': forms.DateInput(attrs={'type': 'date'}),
        }

class TeachersForm(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
        }
