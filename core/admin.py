from django.contrib import admin
from .models import LoginSystem, StudentProfile, TeacherProfile, AdminProfile

from django.contrib import admin
from .models import StudentProfile, TeacherProfile

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'grade', 'school_name', 'points', 'badges', 'streak', 'games_played', 'average_score', 'accuracy_rate')
    search_fields = ('user__username', 'school_name', 'grade')

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'points', 'badges', 'streak', 'games_played', 'average_score', 'accuracy_rate')
    search_fields = ('user__username', 'department')


class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'profile_picture')
    search_fields = ('user__username', 'department')

class LoginSystemAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number','role', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'role')
    list_filter = ('role', 'is_active')

admin.site.register(LoginSystem, LoginSystemAdmin)

admin.site.register(AdminProfile, AdminProfileAdmin)
