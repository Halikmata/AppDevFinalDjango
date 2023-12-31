from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app.models import Teacher, Guardian, Subject, Student, Detention
from app.forms import TeachersForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Teacher
    context_object_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # Teachers
class TeacherList(ListView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'teacher.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(TeacherList, self).get_queryset(*args, **kwargs)
        return qs   
    
class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeachersForm
    template_name = 'add.html'
    success_url = reverse_lazy('teacher-list')
    
    # Students
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'student.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(StudentList, self).get_queryset(*args, **kwargs)
        return qs   
    
    # Guardians
class GuardianList(ListView):
    model = Guardian
    context_object_name = 'guardian'
    template_name = 'guardian.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(GuardianList, self).get_queryset(*args, **kwargs)
        return qs   
    
    # Subjects
class SubjectList(ListView):
    model = Subject
    context_object_name = 'subject'
    template_name = 'subject.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(SubjectList, self).get_queryset(*args, **kwargs)
        return qs   
    
    # Detentions
class DetentionList(ListView):
    model = Detention
    context_object_name = 'detention'
    template_name = 'detention.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(DetentionList, self).get_queryset(*args, **kwargs)
        return qs   