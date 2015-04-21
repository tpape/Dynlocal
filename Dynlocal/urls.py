from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Dynlocal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Admin page
    url(r'^admin/', include(admin.site.urls)),

    # Auth pages
    url('^auth/', include('django.contrib.auth.urls')),

    # RESTFul API URLs
    url('^rest/', include('Applications.api.urls')),

    # Template URLs
    url('^', include('Applications.web.urls')),

]
