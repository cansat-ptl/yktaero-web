"""yktaero URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.news, name='news'),
    path('about/contacts', views.contacts, name='about/contacts'),
    path('about/staff', views.staff, name='about/staff'),
    path('about/partners', views.partners, name='about/partners'),
    path('projects/payloads', views.payloads, name='projects/payloads'),
    path('projects/yktsat', views.yktsat, name='projects/yktsat'),
    path('projects/sounding-rockets', views.rockets, name='projects/sounding-rockets'),
    path('projects/ground-equipment', views.ground, name='projects/ground-equipment'),
    path('admin/', admin.site.urls),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
