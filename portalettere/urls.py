from django.conf.urls import patterns, include, url
from .api import ThreadResource, ContactResource, MessageResource
from .views import ThreadMsgsLW
from .models import Thread
from tastypie.api import Api
from django.views.generic import ListView

from django.contrib import admin
admin.autodiscover()

api = Api(api_name='comm')
api.register(ThreadResource())
api.register(ContactResource())
api.register(MessageResource())

urlpatterns = patterns('',
    url(r'^api/', include(api.urls)),
    url(r'^th/$', ListView.as_view(model=Thread, template_name='threadlist.html')),
    url(r'^th/send/(?P<threadpk>\d+)/$', 'portalettere.views.send_message', name='send_in_thread'),
    url(r'^addthread/$', 'portalettere.views.add_thread', name='add_thread'),
    url(r'^th/(\d+)/$', ThreadMsgsLW.as_view(), name='thread'),
    url(r'^admin/', include(admin.site.urls)),
)
