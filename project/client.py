#import json
#import urllib
#import urllib2
#from urllib2 import urlopen
#
#class ClientAPI(object):
#	def request(self, user):
#				
#		url = "http://api-stage.letsvolley.com/api/devint/Users.php"
#
#		values = {
#			'action' : '5',
#			'userID' : '131905'}
#
#		data = urllib.urlencode(values)
#		req = urllib2.Request(url, data)
#		response = urllib2.urlopen(req)
##		response = urlopen(url, data="action=5", data="userID=131905")
#
#		raw_data = response.read().decode('utf-8')
#		return json.loads(raw_data) #return a python dictionary

import json
from urllib2 import urlopen

class ClientAPI(object):
    def request(self, user):
        url = "https://api.github.com/users/%s" % user
        response = urlopen(url)
		
        raw_data = response.read().decode('utf-8')
        return json.loads(raw_data)
