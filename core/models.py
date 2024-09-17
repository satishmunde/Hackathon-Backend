from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage


class LoginSystem(AbstractUser):
    phone_number = models.CharField(max_length=10)
    access_token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)

    # Define roles as choices
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # Django requires USERNAME_FIELD to be unique
    # USERNAME_FIELD = 'emp_id'

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name','phone_number','role']

    # Helper methods for role-specific access
    def is_admin(self):
        return self.role == 'admin'

    def is_teacher(self):
        return self.role == 'teacher'

    def is_student(self):
        return self.role == 'student'

    # Method to generate unique employee ID


    # Overriding save to automatically assign an emp_id
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} "

    # Instead of deleting, mark the user as inactive
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
        


class StudentProfile(models.Model):
    user = models.OneToOneField(LoginSystem, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    grade = models.CharField(max_length=10)
    school_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='student_pics/', blank=True, null=True)
    
    # Performance tracking fields
    points = models.IntegerField(default=0)
    badges = models.JSONField(default=list)  # Stores badges as a list of strings (badge names)
    streak = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    average_score = models.FloatField(default=0.0)
    accuracy_rate = models.FloatField(default=0.0)  # Percentage of correct answers across all games

    def __str__(self):
        return f"{self.user.username} - Student"

class TeacherProfile(models.Model):
    user = models.OneToOneField(LoginSystem, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    department = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='teacher_pics/', blank=True, null=True)

    # Performance tracking fields (same as StudentProfile)
    points = models.IntegerField(default=0)
    badges = models.JSONField(default=list)
    streak = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    average_score = models.FloatField(default=0.0)
    accuracy_rate = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username} - Teacher"



class AdminProfile(models.Model):
    user = models.OneToOneField(LoginSystem, on_delete=models.CASCADE, limit_choices_to={'role': 'admin'})
    department = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='admin_pics/', blank=True, null=True)
    
    
    
    
    
@receiver(pre_save, sender=StudentProfile)
@receiver(pre_save, sender=TeacherProfile)
@receiver(pre_save, sender=AdminProfile)
def delete_old_profile_picture(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return
    new_file = instance.profile_picture
    old_file = old_instance.profile_picture
    if old_file and old_file != new_file:
        if default_storage.exists(old_file.path):
            default_storage.delete(old_file.path)

@receiver(post_delete, sender=StudentProfile)
@receiver(post_delete, sender=TeacherProfile)
@receiver(post_delete, sender=AdminProfile)
def delete_profile_picture_on_delete(sender, instance, **kwargs):
    if instance.profile_picture and default_storage.exists(instance.profile_picture.path):
        default_storage.delete(instance.profile_picture.path)
