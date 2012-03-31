'''Classes to send stuff, possibly with new methods
   in the future'''
import logging
logger = logging.getLogger(__name__)

class Sender(object):
    

    def send(destination, content):
        raise NotImplementedError('Override this')


class FakeSender(Sender):
    def send(self, destination, content):
        print('Sending to: {0} - {1}'.format(destination, content))

class AsteriskCommandSender(Sender):
    import subprocess
    def send(self, destination, content):
        logger.info('Sending message to {0}'.format(destination))
        out = subprocess.check_output(['sudo', '/usr/sbin/asterisk', '-r' '-x' 'dongle sms dongle0 {0} {1}'.format(destination, content)])
        logger.debug('Returned: {0}'.format(out))
