#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json
import re
import sys
import time

if (len(sys.argv)==1): # If no command line argument is passed, ask for input.
	query = raw_input("Enter Search Query: ").strip() #take song input
	searchterm = '+'.join(query.split()) #add lyrics to it at the end
else:
	query = sys.argv[1:]
	searchterm = '+'.join(query)+'lyrics' # taking the input from command line and adding lyrics at the end.

#Finding video id of first search result
print 'Searching for music...'
url = "https://www.youtube.com/results?search_query="+searchterm # Querying youtube for a lyrics video
html_content = urllib2.urlopen(url) # open the source code of the results page
results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode(encoding='UTF-8')) # use regex to list out all the results
id = results[0] #select first result

headers = { 'User-Agent' : 'Mozilla/5.0' } # So that cloudflare doesn't flag this script as bot

def replace_all_text(text, dic):
	for i, j in dic.iteritems():
		text = text.replace(i, j)
	return text

def youtube2mp3(ylink):
	# Fetch it's properties in json
	info = 'http://www.convertmp3.io/fetch/?format=json&video=https://www.youtube.com/watch?v='+ylink
	removal_text = {"lyrics": "", "Lyrics": "", "(lyrics)": "", "(Lyrics)": "", "HD": "", "HQ": "", "[HQ]": "", "[HD]": ""}
	# Applying User-Agent and getting download links (else it would give error on cloudflare sites)
	page_source = urllib2.urlopen(urllib2.Request(info, None, headers)).read() # Open the page as json, with headers
	in_json = json.loads(page_source) # parse the json
	fname = in_json['title']+'.mp3' # generating filename from video title automatically.
	filename = replace_all_text(fname, removal_text).replace('()','') # removing 'lyrics' from filename, to maintain professionalism :P
	dlink = in_json['link'] # getting key for link in json
	return dlink, filename #return the download link and file name
# Initiating Download
downlink, filename = youtube2mp3(id) # assigning download link and filename
u = urllib2.urlopen(urllib2.Request(downlink, None, headers)) # generating the download link, with headers
print 'Waiting for server...'
time.sleep(3) # download fails sometimes, as the server is busy converting the video, which is not instantaneous. 
print 'Initiating Download, please wait...' 
with open(filename, 'wb') as output: # opening file to write the download
	output.write(u.read()) # begin writing!
print 'Donwload Completed! -> "%s"' % filename