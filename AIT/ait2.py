import sys
import json
import urllib
import urllib2
import requests
from urllib2 import urlopen
import pycurl
import cStringIO

url = ["http://volley-api.devint.selfieclubapp.com/master/", "http://api.letsvolley.com/sc0006/", "http://volley-api.selfieclubapp.com/master/"]
#url_devint = url[0], url_oldprod = url[1], url_newprod = url[2]
api_call = ["users/getactivity", "clubs/get", "clubs/label"]
hmac_id = "HMAC: e318f30beb9c932aec604659fdbea85d2cc89da7cf57d23b8958a9b633dd9dc3+80C8DA5B92AB40C38CCCDDF3C69352B6+80C8DA5B-92AB-40C3-8CCC-DDF3C69352B6"
userID = "userID=155460"
clubID = "clubID=3358"

def getactivity():
	print "------------users/getactivity------------"
	c = pycurl.Curl()
	for i in range(3):
		c.setopt(pycurl.URL, url[i]+api_call[0])
		c.setopt(c.POSTFIELDS, 'lastUpdated=0000-00-00 00:00:00')
		c.setopt(c.POSTFIELDS, userID)
		c.setopt(c.POSTFIELDS, hmac_id)
		c.perform()
		if(c.getinfo(pycurl.HTTP_CODE) == 200):
			print(": Success!")

def clubs_get():
	print "------------clubs/get-----------"
	c = pycurl.Curl()
	for i in range(3):
		c.setopt(pycurl.URL, url[i]+api_call[1])
		c.setopt(c.POSTFIELDS, clubID)
		c.setopt(c.POSTFIELDS, userID)
		c.setopt(c.POSTFIELDS, hmac_id)
		c.perform()
		if(c.getinfo(pycurl.HTTP_CODE) == 200):
			print(": Success!")

def clubs_label():
	print "------------clubs/label-----------"
	c = pycurl.Curl()
	for i in range(3):
		c.setopt(pycurl.URL, url[i]+api_call[2])
		c.setopt(c.POSTFIELDS, hmac_id)
		c.perform()
		if(c.getinfo(pycurl.HTTP_CODE) == 200):
			print(": Success!")

getactivity()
clubs_get()
clubs_label()

'''
	#users/getacivity
	cmd = ['curl', '-X', 'POST', url[i]+api_call[0], '-d', '"lastUpdated=0000-00-00 00:00:00"', '-d', userID, '-H', hmac_id]
	
	#clubs/get
	cmd = ['curl', '-X', 'POST', url[i]+api_call[1], '-d', clubID, '-d', userID, '-H', hmac_id]
	
	#clubs/label
	cmd = ['curl', '-X', 'POST', url[i]+api_call[2], '-H', hmac_id]
'''





