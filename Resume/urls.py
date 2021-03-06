"""Resume URL Configuration

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
from account import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from spec import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('info/<int:applicant_id>', views.info, name="info"),
    path('create', views.create, name="crate"),
    path('create_applicant', views.create, name="create_applicant"),
    path('edit/<int:applicant_id>', views.edit, name="edit"),
    path('delete/<int:applicant_id>', views.delete, name="delete"),
    path('userinfo/', views.user_info, name="userinfo"),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, }),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
