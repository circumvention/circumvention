import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import urllib.request
import json 

import gdata.youtube
import gdata.youtube.service

yt_service = gdata.youtube.service.YouTubeService()


url = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id=gnPPgX1p5lc&key=AIzaSyBpJrEkp6QfLqy1ZPeLeCXLN_eIW_Ir7_w'
key = 'AIzaSyBpJrEkp6QfLqy1ZPeLeCXLN_eIW_Ir7_w'
SnipURL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id=gnPPgX1p5lc&key=AIzaSyBpJrEkp6QfLqy1ZPeLeCXLN_eIW_Ir7_w'

api_service_name = "youtube"
api_version = "v3"


#ViewCount
data = urllib.request.urlopen(url).read()
viewCount = str(json.loads(data)['items'][0]['statistics']['viewCount'])
print(viewCount)
	
#Title View	
data = urllib.request.urlopen(SnipURL).read()
title = str(json.loads(data)['items'][0]['snippet']['title'])
print(title)

request = youtube.videos().update(
        part="id,snippet",
        body={
          "id": "gnPPgX1p5lc",
          "snippet": {
            "title": "test",
            "categoryId": "23"
          }
        }
    )
response = request.execute()
print(response)

print(response)
VideoData()
titleData()
