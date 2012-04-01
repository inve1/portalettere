from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from .models import Thread, Message, Contact
from tastypie import fields
from tastypie.authorization import Authorization
from django.core.urlresolvers import reverse

class ContactResource(ModelResource):
    class Meta:
        queryset = Contact.objects.all()
        fields = ['first_name', 'last_name', 'number']
        filtering = {
            'number': ALL
        }

class ThreadResource(ModelResource):
    msgs_with = fields.ForeignKey(ContactResource, 'msgs_with')

    class Meta:
        queryset = Thread.objects.all()
        resource_name = 'thread'
        filtering = {
            'msgs_with': ALL_WITH_RELATIONS,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte']
        }

class MessageResource(ModelResource):
    thread = fields.ForeignKey(ThreadResource, 'thread')
    class Meta:
        queryset = Message.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post']
        authorization = Authorization()
