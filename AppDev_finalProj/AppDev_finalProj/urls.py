from django.contrib import admin
from django.urls import path
from app import views
from app.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    
    path('teacher_list', views.TeacherList.as_view(), name='teacher-list'),
    path('teacher_list/add', views.TeacherCreateView.as_view(), name='teacher-add'),
    
    path('student_list', views.StudentList.as_view(), name='student-list'),
    
    path('guardian_list', views.GuardianList.as_view(), name='guardian-list'),
    
    path('subject_list', views.SubjectList.as_view(), name='subject-list'),
    
    path('detention_list', views.DetentionList.as_view(), name='detention-list'),
]
