from django.http import HttpResponse,\
     HttpResponseRedirect, HttpResponseForbidden,\
     HttpResponseBadRequest
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .models import Message, Thread, Contact
from .forms import SimpleSendForm
from django.views.generic import ListView


def send_message(request):
    if request.method == 'POST':
        form = SimpleSendForm(request.POST)
        if form.is_valid():
            thread, created = Thread.objects.\
                              get_or_create(msgs_with=Contact.objects.\
                            get(first_name=form.cleaned_data['dest']))
            msg = Message(content=form.cleaned_data['message'],
                            thread=thread, received=False)
            msg.save()
            print('Would have called sudo /usr/sbin/asterisk'
                    '-r -x"dongle sms dongle0 {0} {1}"'.format(msg.number(), msg.content))
    else:
        form = SimpleSendForm()

    return render_to_response('simplesend.html', {
            'form': form
            },
        context_instance=RequestContext(request))


class ThreadMsgsLW(ListView):
    context_object_name = 'messages'
    model = Message
    template_name = "msgs.html"

    def get_queryset(self):
        self.thread = get_object_or_404(Thread, pk=self.args[0])
        return Message.objects.filter(thread=self.thread)

    def get_context_data(self, **kwargs):
        context = super(ThreadMsgsLW, self).get_context_data(**kwargs)
        context['talkingto'] = self.thread.msgs_with
        return context
