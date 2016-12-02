"""baatKar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse

urlpatterns = [
    # url(r'^auth/', include('socialauthapp.urls', namespace='socialauthapp')),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('chatapp.urls', namespace='chatapp')),
    url(r'^profile/', include('chatapp.urls', namespace='chatapp')),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)