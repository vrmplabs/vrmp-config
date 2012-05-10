import urllib2

httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler,httpsHandler)


urllib2.install_opener(opener)
#res = urllib2.urlopen('https://172.16.0.11:8139/production/run/no_key','')



req = urllib2.Request('https://172.16.0.11:8139/production/run/no_key')
#req.add_header('Content-Type','text/pson')
req.add_header('Accept','*/*')
#req.add_header('Content-Length','2')
#req.get_method = lambda: 'PUT'
print(req.get_method())


#res = opener.open(req)
res = urllib2.urlopen(req)
print(res.info())
results = res.read()
print('Result:\r\n'+results)
print 'Done'
