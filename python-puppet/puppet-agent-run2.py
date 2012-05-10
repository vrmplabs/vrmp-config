import urllib2
import urllib

req_data = {'foo':'bar'}
encoded_req_data = urllib.urlencode(req_data)
headers = {'Accept':'pson'}
req = urllib2.Request('https://172.16.0.11:8139/production/run/no_key',encoded_req_data,headers)
#req.add_header('Content-Type','text/pson')
#req.add_header('Accept','pson')
print(req.get_method())
print(req.get_data())
res = urllib2.urlopen(req,encoded_req_data)
result = res.read()
print('Result:\r\n'+result)
res.close()
print 'Done'
