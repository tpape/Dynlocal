from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Dynlocal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Admin page
    url(r'^admin/', include(admin.site.urls)),

    # Auth pages
    url('^', include('django.contrib.auth.urls'))

    # Template URLs

    # RESTFul API URLs
]
