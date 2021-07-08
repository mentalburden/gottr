#!/usr/bin/python3

import json
import glob
import time
import requests

globaldelay = 0.8
targetfile = "unique_usernames.txt"


#Need to spoof ios or android UA and supply full standard browser header for usernamechecks
#samsung = Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36
#lg = Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36
#iphone = Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1

def writetofile(thisuser, thisjson):
	cleanfile = str(thisuser[:1]) + "-userprofiles.txt"
	with open(cleanfile, "a+") as thisfile:
		thisfile.write(json.dumps(thisjson) + "\n")
		print(thisuser)


def usercheck(thisuser):
	thisdict = {thisuser: {}}
	myheader = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
			"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1",
			"Connection": "keep-alive",
			}
  #disect this path and the return json later when you get into the media.getter.com scrape
  #should be able to pull all media paths easily without recurse
	thispath = "https://api.gettr.com/u/user/" + thisuser + "/posts?offset=0&max=2000&dir=fwd&incl=posts%7Cstats%7Cuserinfo%7Cshared%7Cliked&fp=f_ul"
	req = requests.get(thispath, headers=myheader)
	thisdict['thisuser'] = json.loads(req.text)
	checklen = len(thisdict['thisuser']['result']['data']['list'])
	if checklen >= 1:
		time.sleep(globaldelay)
		return thisdict

#main here
with open(targetfile, 'r') as tfile:
	biglines = tfile.readlines()
	for username in biglines:
		cleanuser = username.replace('\n', "")
		checkeduser = usercheck(cleanuser)
		if checkeduser is not None:
			writetofile(cleanuser, checkeduser)
