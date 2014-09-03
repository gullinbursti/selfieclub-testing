import sys
import json
import urllib
import urllib2
import requests
from urllib2 import urlopen
import pycurl
import cStringIO

#url[0] = url of devint, url[1] = url of oldprod, url[2] = url of newprod
url = ["http://volley-api.devint.selfieclubapp.com/master/", "http://api.letsvolley.com/sc0006/", "http://volley-api.selfieclubapp.com/master/"]

#types of api calls
api_call = ["users/getactivity", "clubs/get", "clubs/label"]

#for hmac id
hmac_id = "HMAC: e318f30beb9c932aec604659fdbea85d2cc89da7cf57d23b8958a9b633dd9dc3+80C8DA5B92AB40C38CCCDDF3C69352B6+80C8DA5B-92AB-40C3-8CCC-DDF3C69352B6"

#for userID
userID = "userID=155460"

#for clubID
clubID = "clubID=3358"

#each REST call has it's own function
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
                else:
                        print(" HTTP return code is not 200")

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
		else:
			print(" HTTP return code is not 200")

def clubs_label():
	print "------------clubs/label-----------"
	c = pycurl.Curl()
	for i in range(3):
		c.setopt(pycurl.URL, url[i]+api_call[2])
		c.setopt(c.POSTFIELDS, hmac_id)
		c.perform()
		if(c.getinfo(pycurl.HTTP_CODE) == 200):
			print(": Success!")
                else:
                        print(" HTTP return code is not 200")

#main function that executes the REST calls
def main():
	getactivity()
	clubs_get()
	clubs_label()
main()

