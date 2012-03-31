from tastypie.resources import ModelResource
from .models import Thread, Message, Contact


class ThreadResource(ModelResource):
    class Meta:
        queryset = Thread.objects.all()
        resource_name = 'thread'
