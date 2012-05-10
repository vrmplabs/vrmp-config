import urllib
import urllib2


req = urllib2.Request('https://127.0.0.1:8140/production/status/puppetclient')
req.add_header('Content-Type','text/pson')
req.add_header('Accept','pson')
#print(req.get_method())
try:
	res = urllib2.urlopen(req)
except urllib2.URLError,e:
	print 'URLError Occured.'
	print e.code
	print e.read()
except HTTPError,e:
	print 'HTTPError Occured.'
	print e.code
	print e.read()
else:
	result = res.read()
	print('Result:\r\n'+result)
print 'Done'
