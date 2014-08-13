import json
from urllib2 import urlopen

class ClientAPI(object):
    def request(self, user):
        url = "api.devint.selfieclubapp.com/club/%s" % user
        response = urlopen(url)
		
        raw_data = response.read().decode('utf-8')
        return json.loads(raw_data)
