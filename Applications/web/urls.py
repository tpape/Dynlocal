from django.conf.urls import include, url
from Applications.web import views

urlpatterns = [
    # Template URLs
    url(r'^$', views.index),
    url(r'contrib/$', views.register),
    url(r'contrib/register$',views.register),
    url(r'contrib/login$', views.user_login),
#    url(r'register/$', views.register),
]
