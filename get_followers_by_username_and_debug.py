#!/usr/bin/python3

import json
import time
import requests

checkuser = "validtarget-here"
offsetmaxglobal = 10 #10000 followers = 10, its an offset of 1000 per GET against the followers path
#if <1000 users use getfollowersfor() instead, 
----------------------------------------------------------------------------------------------------#fix this later with user.follower count check

globaldelay = 0.6 #0.8 is most stable from a DO wan ip

def appendtofile(towrite):
        with open(checkuser + "_users.txt", "a+") as thisfile:
                thisfile.write(json.dumps(towrite) + "\n")
                thisfile.close()

def getpost(thishash):
        thisurl = "https://api.gettr.com/u/post/" + thishash
        myheader = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        req = requests.get(thisurl, headers=myheader)
        jason = json.loads(req.text)
        outdict = {thishash: jason}
        return outdict

def getcomment(thishash):
        thisurl = "https://api.gettr.com/u/post/" + thishash
        myheader = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        req = requests.get(thisurl, headers=myheader)
        jason = json.loads(req.text)
        print(jason)

def getfollowerswithoffsetfor(username, offsetint):
        outdict = {"usernames":[]}
        offmin = offsetint * 1000
        offmax = (offsetint * 1000) * 2
        thisurl = "https://api.gettr.com/u/user/" + username + "/followers/?offset=" + str(offmin) + "&max=" + str(offmax)
        myheader = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        req = requests.get(thisurl, headers=myheader)
        jason = json.loads(req.text)
        followlist = jason['result']['data']['list']
        for user in followlist:
                outdict['usernames'].append(user)
        appendtofile(outdict)
        time.sleep(globaldelay)

def getfollowersfor(username):
        outdict = {"usernames":[]}
        thisurl = "https://api.gettr.com/u/user/" + username + "/followers/"
        myheader = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        req = requests.get(thisurl, headers=myheader)
        jason = json.loads(req.text)
        followlist = jason['result']['data']['list']
        for user in followlist:
                outdict['usernames'].append(user)
        appendtofile(outdict)
        time.sleep(globaldelay)

#main here
#appendtofile(getpost("valid-6-char-hash-here"))
for i in range(1, offsetmaxglobal):
        getfollowerswithoffsetfor(checkuser, i)
#getfollowersfor(checkuser)

