from django.conf.urls import url
from django.contrib import admin

from .views import (
        profile,
        Home,
        Post,
        Messages
)

urlpatterns = [
    url(r'^$', profile, name='profile'),
    url(r'^home/(?P<receiver>[A-Za-z0-9]+)$', Home, name='home'),
    url(r'^post/$', Post, name='post'),
    url(r'^messages/(?P<receiver>[A-Za-z0-9]+)$',Messages, name='messages'),

]