"""
URL configuration for mentor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from .views import Home
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from authy.views import user_profile
from classroom.views import index,Categories
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('course_recommendation/', include('course_recommendation.urls')),
    path('courses/', include('courses.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('job_recommendation/', include('job_recommendation.urls')),
    path('resume_building/', include('resume_building.urls')),
    path('roadmaps/', include('roadmaps.urls')),
    path('skill_assessment/', include('skill_assessment.urls')),

    path('user/', include('authy.urls')),
    path('course/', include('classroom.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('direct/', include('direct.urls')),
    path('<username>', user_profile, name='profile'),
    path('user/login', index, name='index')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



