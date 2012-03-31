from django.conf.urls import patterns, include, url
from .api import ThreadResource
from .views import ThreadMsgsLW

from django.contrib import admin
admin.autodiscover()

thread_resouce = ThreadResource()

urlpatterns = patterns('',
    url(r'^simplesend/$', 'portalettere.views.send_message', name='simplesend'),
    # url(r'^portalettere/', include('portalettere.foo.urls')),

    url(r'^thread/', include(thread_resouce.urls)),
    url(r'^th/(\d+)/$', ThreadMsgsLW.as_view()),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
