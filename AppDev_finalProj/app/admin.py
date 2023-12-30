from django.contrib import admin
from .models import Guardian, Student, Teacher, Detention, Subject

@admin.register(Guardian)
class GuardiansAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'is_emergency_contact']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']

@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'email', 'admission_date', 'guardian', 'is_active']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']
    list_filter = ['is_active', 'admission_date']

@admin.register(Teacher)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthdate', 'subject', 'email', 'joining_date', 'is_active']
    search_fields = ['name', 'email', 'phone_number']
    list_filter = ['is_active', 'joining_date']

@admin.register(Detention)
class DetentionsAdmin(admin.ModelAdmin):
    list_display = ['student', 'teacher', 'incident_time', 'fines', 'is_resolved']
    search_fields = ['student__first_name', 'student__last_name', 'teacher__name', 'reason']
    list_filter = ['is_resolved', 'incident_time']
    
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name', 'code', 'prerequisite', 'units', 'lab']
    search_fields = ['subject_name', 'code']
    list_filter = ['lab']
    raw_id_fields = ['prerequisite']
