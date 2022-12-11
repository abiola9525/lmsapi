"""lmsApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from ensurepip import version
from django.contrib import admin
from matplotlib.pyplot import title
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from users.views import LogoutAPIView, LoginAPIView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/login/', LoginAPIView.as_view(), name="login"),
    path('users/logout/', LogoutAPIView.as_view(), name="logout"),
    path('assignments/', include('ass.assignments.urls')),
    path('graded-assignments/', include('ass.graded_assignments.urls')),
    path('users/', include('users.urls')),
    path('social_auth/', include(('social_auth.urls', 'social_auth'),
                                 namespace="social_auth")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('feedback/', include('feedback.urls')),
    path('course', include('course.urls')),
    path('docs/', include_docs_urls(title='LMSAPI')),
    path('schema', get_schema_view(
        title="LMSAPI",
        description="API for a LMSAPI",
        version="1.0.0"
    ), name='openapi-schema'),
    
]
