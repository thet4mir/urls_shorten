from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.url_create),
    re_path(r'^(?P<short_code>\w+)/$', views.url_redirect),
]
