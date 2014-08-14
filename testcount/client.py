import sys
import json
import urllib
import urllib2
import requests
from urllib2 import urlopen

def clubname():					
	url = "http://api.devint.selfieclubapp.com/club/"
	r = requests.get(url)
	data = r.json()
	reload(sys)
	sys.setdefaultencoding("utf-8")
	p = open("./tests/resources/users/club.txt", "w")	
	count_t = 0	
	while 1:
		dict = data['results']
		for i in range(0, len(dict)):
			p.write(str(dict[i]['name']) + '\n')

		url = data['next']
		if data['next'] == None:
			break
		r = requests.get(url)
		data = r.json()
		count_t = count_t + 1

	#f = open("./tests/resources/users/test_user", "w")
	#f.write(str(count_t))

def count():
	url = "http://api.devint.selfieclubapp.com/club/"
	r = requests.get(url)
	data = r.json()
	reload(sys)
	sys.setdefaultencoding("utf-8")

	count = data['count']
	return count
