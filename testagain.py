import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import urllib.request
from pyyoutube import Api
import json





url = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id=gnPPgX1p5lc&key=AIzaSyBpJrEkp6QfLqy1ZPeLeCXLN_eIW_Ir7_w'
key = 'AIzaSyBpJrEkp6QfLqy1ZPeLeCXLN_eIW_Ir7_w'
SnipURL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id=gnPPgX1p5lc&key=AIzaSyBpJrEkp6QfLqy1ZPeLeCXLN_eIW_Ir7_w'

api_service_name = "youtube"
api_version = "v3"

api = Api(api_key=key )


#ViewCount
data = urllib.request.urlopen(url).read()
viewCount = str(json.loads(data)['items'][0]['statistics']['viewCount'])
print(viewCount)


video = api.get_video_by_id(video_id="gnPPgX1p5lc")

print(video)

#request = youtube.videos().update(
 #       part="id,snippet",
 #       body={
 #         "id": "gnPPgX1p5lc",
 #         "snippet": {
 #           "title": "test1",
 #           "categoryId": "23"
 #         }
 #       }
 #   )
response = request.execute()
print(response)
