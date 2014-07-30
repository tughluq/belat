from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'toupiao.views.home', name='home'),
    # url(r'^toupiao/', include('toupiao.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^polls/', include('polls.urls')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    #url(r'^polls/', include('polls.urls', namespace="polls")),
)
