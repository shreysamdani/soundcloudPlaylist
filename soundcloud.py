from __future__ import print_function
import requests
import sys
import json
import os
import urllib

playlist = sys.argv[1]
r = requests.get(playlist)
html = r.text

# extract the tracks
jsonstr = html.split(',"tracks":')[-1].split(',"track_count"')[0]
jsonstr = json.loads(jsonstr)

def getTrackUrl(trackID):
	r = requests.get("https://api.soundcloud.com/i1/tracks/" + str(trackID) + "/streams?client_id=NZtb1cCBbHFHV67f1Fp9jkGKog0H4StA")
	links = json.loads(r.text)
	return links["http_mp3_128_url"]

def getTrackData(trackID):
	r = requests.get("https://api-v2.soundcloud.com/tracks?ids=" + str(trackID) + "&client_id=NZtb1cCBbHFHV67f1Fp9jkGKog0H4StA")
	info = json.loads(r.text)[0]
	print(info)
	return info["title"], info[""]

dir = playlist.split("/")[-1]
if not os.path.exists(playlist.split("/")[-1]):
	os.mkdir(dir)

try:
	retriever = urllib.urlretrieve
except AttributeError:
	retriever = urllib.request.urlretrieve

for track in jsonstr:
	url = getTrackUrl(track["id"])
	filename = dir + "/" + getTrackTitle(track["id"]) + ".mp3"
	print("Downloading and saving", filename, "...", end = " ")
	retriever(url, filename)
	print("Done!")