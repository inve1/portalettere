""" Models for the portalettere
"""

from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.CharField(max_length=30)

    def __unicode__(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)


class Thread(models.Model):
    msgs_with = models.ForeignKey(Contact)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'With: {0}'.format(self.msgs_with)

class Message(models.Model):
    content = models.TextField()
    thread = models.ForeignKey(Thread)
    received = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def number(self):
        return self.thread.msgs_with.number

    def __unicode__(self):
        if not self.received:
            toprint = 'To'
        else:
            toprint = 'From'
        return u'{2}: {0} - {1}'.format(self.number(), self.content, toprint)
