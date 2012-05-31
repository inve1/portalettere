'''Very stupid script to use the api from asterisk'''
import sys
import requests
import simplejson
import base64

print 'hallo'
if len(sys.argv) != 4:
    print('''Usage:
            {0} ip_of_service:port number message'''.format(sys.argv[0]))
else:
    r = requests.get('http://{0}/api/comm/thread/?msgs_with__number={1}'
            '&format=json'.format(sys.argv[1], sys.argv[2].replace('+', '%2B')))
#    print r.text
    resuri = simplejson.loads(r.text)['objects'][0]['resource_uri']
    r2 = requests.post('http://{0}/api/comm/message/'.format(sys.argv[1]),
            headers={'Content-type': 'application/json'},
            data=simplejson.dumps({"content": base64.decodestring(sys.argv[3]).decode('utf-8'), "thread": resuri}))

