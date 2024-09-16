from django.contrib import admin
from .models import LoginSystem, StudentProfile, TeacherProfile, AdminProfile

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'grade', 'school_name', 'profile_picture')
    search_fields = ('user__username', 'grade', 'school_name')

class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'profile_picture')
    search_fields = ('user__username', 'department')
    # filter_horizontal = ('subjects',)

class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'profile_picture')
    search_fields = ('user__username', 'department')

class LoginSystemAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number','role', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'role')
    list_filter = ('role', 'is_active')

admin.site.register(LoginSystem, LoginSystemAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(TeacherProfile, TeacherProfileAdmin)
admin.site.register(AdminProfile, AdminProfileAdmin)
