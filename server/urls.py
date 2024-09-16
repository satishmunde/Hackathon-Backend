"""
URL configuration for HMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path ,include
from . import views
from django.conf.urls.static import static
import debug_toolbar
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib.auth.decorators import login_required

# Define the schema view
schema_view = get_schema_view(
    openapi.Info(
        title="HOTEL SYSTEM API DOUMENTATION PAGE",
        default_version="v1",
        description="Description of your API",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,  
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[]
)



urlpatterns = [
    # URL pattern for api Dacumentations 
    path('swagger<format>/', login_required(schema_view.without_ui(cache_timeout=0)), name='schema-json'),
    path('swagger/', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    path('', login_required(schema_view.with_ui('redoc', cache_timeout=0)), name='schema-redoc'),
    
    # URL for  Admin panel 
    path("admin/", admin.site.urls),
    
    # URL for Debug toolbar
    path('__debug__/', include(debug_toolbar.urls)),
    
    # URL for API endpoints
    path('api/', include('api.urls')),

    
    
    path("login/", views.login),
    # path("register/", views.register),
    # path("forget-password/", views.forget_password),
    path('logout/', views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    # path("send_email", views.email),
    
    

]


# Additional configurations
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)