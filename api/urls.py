"""
URL configuration for HMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    # Authentication URLs
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    # Core app URLs with prefixes
    path('profile/', include('core.urls')),  # Ensure core.urls has a student namespace
    path('community/', include('community.urls')),
    path('lms/', include('lms_system.urls')),

]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
