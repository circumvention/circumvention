import os
import time
import json

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import urllib
import sys



scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT.json"
    
    url = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id=gNMBTjDT9ew&key=AIzaSyDzexaJCbzger34TtAeWgkVebossSpU_XI'
    
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    data = urllib.request.urlopen(url).read()
    viewCount = str(json.loads(data)['items'][0]['statistics']['viewCount'])
    running = True
    while running == True:  
     for remaining in range(130, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("Title changing... {:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
     print('Title Changing Done.')
     request = youtube.videos().update(
            part="snippet",
            body={
            "id": "gNMBTjDT9ew",
            "snippet": {
                "title": "if this video has " + str(viewCount) + " views you're cool",
                "categoryId": "23"
            }
          }
        )
     response = request.execute()
        

if __name__ == "__main__":
    main()
