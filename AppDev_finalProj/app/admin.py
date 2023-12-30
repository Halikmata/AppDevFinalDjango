from django.contrib import admin
from .models import Guardians, Students, Teachers

@admin.register(Guardians)
class GuardiansAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'is_emergency_contact']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'email', 'admission_date', 'is_active']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']
    list_filter = ['is_active', 'admission_date']

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthdate', 'subject', 'email', 'joining_date', 'is_active']
    search_fields = ['name', 'email', 'phone_number']
    list_filter = ['is_active', 'joining_date']
