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

    # url(r'^create/$', post_create),
    # url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    # url(r'^posts/$', "<appname>.views.<function_name>"),
]