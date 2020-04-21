

import os
import time
import json

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT.json"
    
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    data = urllib.request.urlopen(url).read()
    viewCount = str(json.loads(data)['items'][0]['statistics']['viewCount'])

while True:  
    time.sleep(1)
    request = youtube.videos().update(
        part="snippet",
        body={
          "id": "gnPPgX1p5lc",
          "snippet": {
            "title": "if this video has " + str(viewCount) + "you're cool",
            "categoryId": "23"
          }
        }
    )
    response = request.execute()

    print('execute succesful')

if __name__ == "__main__":
    main()
