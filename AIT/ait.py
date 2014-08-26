import sys
import json
import urllib
import urllib2
import requests
from urllib2 import urlopen
import subprocess

def get_curlcommands_returndata():
	url = ["http://volley-api.devint.selfieclubapp.com/master/", "http://api.letsvolley.com/sc0006/", "http://volley-api.selfieclubapp.com/master/"]
	#url_devint = url[0]
	#url_oldprod = url[1]
	#url_newprod = url[2]
	hmac_id = "HMAC: e318f30beb9c932aec604659fdbea85d2cc89da7cf57d23b8958a9b633dd9dc3+80C8DA5B92AB40C38CCCDDF3C69352B6+80C8DA5B-92AB-40C3-8CCC-DDF3C69352B6"
	api_call = ["users/getactivity", "clubs/get", "clubs/label"]
	userID = "userID=155460"
	clubID = "clubID=3358"

	#users/getacivity
	print "------------users/getactivity------------"
	for i in range(0,3):
		cmd = ['curl', '-X', 'POST', url[i]+api_call[0], '-d', '"lastUpdated=0000-00-00 00:00:00"', '-d', userID, '-H', hmac_id]
		p = subprocess.Popen(cmd, stdout = subprocess.PIPE)
		result = p.stdout.read()
		print result
		print "\n"
	
	#clubs/get
	print "------------clubs/get-----------"
	for i in range(0,3):
		cmd = ['curl', '-X', 'POST', url[i]+api_call[1], '-d', clubID, '-d', userID, '-H', hmac_id]
		p = subprocess.Popen(cmd, stdout = subprocess.PIPE)
		result = p.stdout.read()
		print result
		print "\n"
	
	#clubs/label
	print "------------clubs/label-----------"
	for i in range(0,3):
		cmd = ['curl', '-X', 'POST', url[i]+api_call[2], '-H', hmac_id]
		p = subprocess.Popen(cmd, stdout = subprocess.PIPE)
		result = p.stdout.read()
		print result
		print "\n"

get_curlcommands_returndata()
