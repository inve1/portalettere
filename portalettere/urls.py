from django.conf.urls import patterns, include, url
from .api import ThreadResource
from .views import ThreadMsgsLW
from .models import Thread
from django.views.generic import ListView

from django.contrib import admin
admin.autodiscover()

thread_resouce = ThreadResource()

urlpatterns = patterns('',
    url(r'^thread/', include(thread_resouce.urls)),
    url(r'^th/$', ListView.as_view(model=Thread, template_name='threadlist.html')),
    url(r'^th/send/(?P<threadpk>\d+)/$', 'portalettere.views.send_message', name='send_in_thread'),
    url(r'^addthread/$', 'portalettere.views.add_thread', name='add_thread'),
    url(r'^th/(\d+)/$', ThreadMsgsLW.as_view(), name='thread'),
    url(r'^admin/', include(admin.site.urls)),
)
