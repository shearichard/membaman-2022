"""membaman URL Configuration

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
from django.conf.urls import include, re_path 
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
admin.site.site_header = 'MembaMan Administration Area'
admin.site.site_title = 'MembaMan Admin'

urlpatterns = [ 
    re_path(r'^$', TemplateView.as_view(template_name='index.html'), name='membamanindex'),
    re_path(r'^fees/', include('fees.urls', 'fees')),
    re_path(r'^members/', include('members.urls', 'members')),
    re_path(r'^admin/', admin.site.urls),
]

