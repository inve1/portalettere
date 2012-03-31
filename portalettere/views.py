from django.http import HttpResponse,\
     HttpResponseRedirect, HttpResponseForbidden,\
     HttpResponseBadRequest
from django.shortcuts import render_to_response, get_object_or_404,\
                            redirect
from django.template import RequestContext
from .models import Message, Thread, Contact
from .forms import SimpleSendForm
from django.views.generic import ListView
from django.conf import settings


def send_message(request, threadpk):
    if request.method == 'POST':
        form = SimpleSendForm(request.POST)
        if form.is_valid():
            thread = get_object_or_404(Thread, pk=threadpk)
            msg = Message(content=form.cleaned_data['message'],
                            thread=thread, received=False)
            msg.save()
            sender = settings.MESSAGE_SENDER()
            sender.send(thread.msgs_with.number, msg.content)
            return redirect('thread', threadpk)
    else:
        return HttpResponseBadRequest('No gets here')

def add_thread(request):
    pass


class ThreadMsgsLW(ListView):
    context_object_name = 'messages'
    model = Message
    template_name = 'msgs.html'

    def get_queryset(self):
        self.thread = get_object_or_404(Thread, pk=self.args[0])
        return Message.objects.filter(thread=self.thread)

    def get_context_data(self, **kwargs):
        context = super(ThreadMsgsLW, self).get_context_data(**kwargs)
        context['talkingto'] = self.thread.msgs_with
        context['thread'] = self.thread
        context['form'] = SimpleSendForm()
        return context
