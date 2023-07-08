"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from core.urls import urlpatterns as core_urls
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
# from core.views import google_auth_complete

urlpatterns = [
    path('', include(core_urls)),
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    # path('complete/google/', google_auth_complete, name='social:complete_google'),
] 

urlpatterns += i18n_patterns(
    path('', include(core_urls)),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)