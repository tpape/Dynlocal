from django.conf.urls import include, url
from Applications.web import views

urlpatterns = [
    # Template URLs
    url(r'^$', views.index)
]
