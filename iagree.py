from tkinter import *
import urllib.request
import json 

url = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id=gnPPgX1p5lc&key=AIzaSyDzexaJCbzger34TtAeWgkVebossSpU_XI'
key = 'AIzaSyDzexaJCbzger34TtAeWgkVebossSpU_XI'
SnipURL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id=gnPPgX1p5lc&key=AIzaSyDzexaJCbzger34TtAeWgkVebossSpU_XI'

def VideoData():
	data = urllib.request.urlopen(url).read()
	
	viewCount = str(json.loads(data)['items'][0]['statistics']['viewCount'])
	print(viewCount)
	
def titleData():
	data = urllib.request.urlopen(SnipURL).read()
	
	title = str(json.loads(data)['items'][0]['snippet']['title'])
	print(title)


VideoData()
titleData()
