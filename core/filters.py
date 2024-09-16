import django_filters
from .models import LoginSystem, StudentProfile, TeacherProfile, AdminProfile

class LoginSystemFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')  # Example of case-insensitive partial match
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    phone_number = django_filters.CharFilter(lookup_expr='icontains')
    role = django_filters.ChoiceFilter(choices=LoginSystem.ROLE_CHOICES)  # Assuming role is a choice field

    class Meta:
        model = LoginSystem
        exclude = ['profile_image', 'access_token', 'refresh_token']  # Exclude sensitive fields


class StudentFilter(django_filters.FilterSet):
    grade = django_filters.CharFilter(lookup_expr='icontains')
    school_name = django_filters.CharFilter(lookup_expr='icontains')
    user__username = django_filters.CharFilter(lookup_expr='icontains')  # Filtering based on related fields
    user__email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = StudentProfile
        fields = ['grade', 'school_name', 'user']


class TeacherFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(lookup_expr='icontains')
    user__username = django_filters.CharFilter(lookup_expr='icontains')  # Filtering based on related fields
    user__email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TeacherProfile
        fields = ['department', 'user']


class AdminFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(lookup_expr='icontains')
    user__username = django_filters.CharFilter(lookup_expr='icontains')  # Filtering based on related fields
    user__email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = AdminProfile
        fields = ['department', 'user']
