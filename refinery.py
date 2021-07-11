#!/usr/bin/python3

import re
import os.path
import json
import glob
import datetime


def cleanjsonfromrawprofile(afile):
	with open(afile, "r") as thisfile:
		biglines = thisfile.readlines()
		for line in biglines:
			cleanline = line.replace("\n", '')
			jason = json.loads(cleanline)
			themkeys = list(jason.keys())
			thisuser = themkeys[0]
			outdict = {thisuser: {}, "posts": [] }
			for key, val in jason['thisuser']['result']['aux']['post'].items():
				try:
					if len(val["imgs"]) >= 1:
						images = val['imgs']
				except:
					images = ['no-img']
				try:
					if len(val["txt"]) >= 1:
						text = val['txt']
						urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', text)
						if len(urls[0]) >= 2:
							haslinks = True
						else:
							haslinks = False
				except:
					text = 'no-txt'
					haslinks = False
					urls = ['nolinks']
				try:
					if len(val['dsc']) >= 1:
						desc = val['dsc']
				except:
					desc = 'no-dsc'
				try:
					if len(val['ttl']) >= 1:
						title = val['ttl']
				except:
					title = "no-ttl"
				try:
					if len(val['prevsrc']) >= 1:
						preview = "link#" + val['prevsrc']
				except:
					preview = "no-prevsrc"
				try:
					if len(str(val['cdate'])) >= 1:
						#ctime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(val['cdate']))
						#etint = int(val['cdate'])
						#ctime = datetime.datetime.fromtimestamp(etint).strftime('%c')
						ctime = val['cdate']
				except:
					ctime = 'no-time'
				try:
					avatarimg = jason['thisuser']['result']['aux']['uinf'][thisuser]['ico']
				except:
					avatarimg = "noimg"
				try:
					bgimg = jason['thisuser']['result']['aux']['uinf'][thisuser]['bgimg']
				except:
					bgimg = "noimg"
				try:
					following = list(jason['thisuser']['result']['aux']['uinf'].keys())
					#following.remove(thisuser)
				except:
					following = ['nofollowers']
				try:
					thispost = {val["_id"]: {'images':images , 'txt': text, 'haslinks': haslinks, 'links': [urls], 'dsc': desc, 'ttl': title, 'ctime': ctime, 'prvsrc': preview}}
					outdict['avatarimg'] = avatarimg
					outdict['bgimg'] = bgimg
					outdict['following'] = following
					outdict['posts'].append(thispost)
				except:
					print("bad record for " + thisuser)
			#print(json.dumps(outdict, indent=2))
			cleanoutfile = "./outjsons/" + str(afile[0]) + "-username-profiles.json"
			outfile = open(cleanoutfile, 'a+')
			outfile.write(json.dumps(outdict, indent=1))
			outfile.close()
#main here
for file in glob.glob("*.txt"):
	print(file)
	cleanjsonfromrawprofile(file)
