from django.urls import include, path, re_path
from django.contrib import admin

from .views import (
    post_list,
    post_Create,
    post_detail,
    post_update,
    post_delete,
)

app_name = 'posts'

urlpatterns = [
    path('', post_list, name='list'),
    re_path(r'^create/$', post_Create),
    re_path(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #path('posts/', "<appname>.views.<function_name>"),
]
