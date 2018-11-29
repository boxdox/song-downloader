#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name: Song Downloader (from Youtube :P)
# Author: Vaibhav Kandwal
# Usage: song-downloader.py song name here
# Version: 1.1? Maybe
# License: Educational Purpose Only, though it is MIT Licensed

import urllib2
import json
import re
import sys
import time

if (len(sys.argv)==1): 
	while True:
		query = raw_input("Enter Search Query: ").strip()
		if len(query)!=0:
			searchterm = '+'.join(query.split())+'lyrics' # add lyrics word in the end
			break
		else:
			print "Please type something, I am not a magician!"
else:
	query = sys.argv[1:]
	searchterm = '+'.join(query)+'lyrics'

# Querying Youtube for video id of first search result
print 'Searching for music...'
search_url = "https://www.youtube.com/results?search_query="+searchterm
html_content_of_result_page = urllib2.urlopen(search_url)
results_list = re.findall(r'href=\"\/watch\?v=(.{11})', html_content_of_result_page.read().decode(encoding='UTF-8'))
video_id = results_list[0]

headers = { 'User-Agent' : 'Mozilla/5.0' } # So that cloudflare doesn't flag this script as bot

def replace_all_text(text, dictionary): # This is a simple function that replaces text based on dictionary. Credits: https://stackoverflow.com/a/6117042/9209803
	for i, j in dictionary.iteritems():
		text = text.replace(i, j)
	return text

def youtube2mp3(ylink): # Youtube to mp3 function, using convertmp3.io's api! Thanks!

	video_info_in_json_url = 'http://www.convertmp3.io/fetch/?format=json&video=https://www.youtube.com/watch?v='+ylink
	text_to_remove_from_name = {"lyrics": "", "Lyrics": "", "(lyrics)": "", "(Lyrics)": "", "HD": "", "HQ": "", "[HQ]": "", "[HD]": "", "(Lyric Video)":"","<":"",">":"",":":"",'"':'',"/":"","\\":"","|":"","?":"","*":""} # this is the dictionary for replacing text.

	# Applying User-Agent and getting download links (else it would give error on cloudflare sites)
	video_info_in_json = json.loads(urllib2.urlopen(urllib2.Request(video_info_in_json_url, None, headers)).read())
	filename = replace_all_text(video_info_in_json['title'], text_to_remove_from_name).replace('()','').strip()+'.mp3'.encode(encoding='UTF-8',errors='strict')
	download_link_from_json = video_info_in_json['link']
	return download_link_from_json, filename

# Initiating Download
download_link_from_json, filename = youtube2mp3(video_id)
final_download_url = urllib2.urlopen(urllib2.Request(download_link_from_json, None, headers)) # generating the download link, with headers
print 'Waiting for server...'
time.sleep(3) # download fails sometimes, as the server is busy converting the video, which is not instantaneous. 
print 'Initiating Download, please wait...' 
with open(filename, 'wb') as output:
	output.write(final_download_url.read())
print 'Donwload Completed! -> "%s"' % filename
