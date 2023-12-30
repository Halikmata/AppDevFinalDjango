from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Guardian(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    is_emergency_contact = models.BooleanField(default=False)
    number_of_children = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    prerequisite = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    units = models.IntegerField()
    lab = models.BooleanField(default=False)

    def __str__(self):
        return self.subject_name

class Student(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    guardian = models.ForeignKey(Guardian, on_delete=models.SET_NULL, null=True, blank=True)
    admission_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    teachers = models.ManyToManyField('Teacher', related_name='students_taught', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Teacher(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    experience_years = models.PositiveIntegerField(null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    students = models.ManyToManyField(Student, related_name='teachers_taught', blank=True)
    notes = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='teacher_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Detention(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    incident_time = models.DateTimeField()
    fines = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} Detention"

    class Meta:
        ordering = ['-incident_time']
        
