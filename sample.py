scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    import os
    import time
    import json
    import google_auth_oauthlib.flow
    import googleapiclient.discovery
    import googleapiclient.errors
    import urllib
    import sys
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_497488498026-npagls46cartolabbib43c0i1ef65r0j.apps.googleusercontent.com.json"
    
    url = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id=gnPPgX1p5lc&key=AIzaSyDFG3fjePXQkGJAA-3u72XhYKZCj3s7Mjw'
    
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
                "id": "gnPPgX1p5lc",
                "snippet": {
                    "title": "if this video has " + str(viewCount) + " views you're cool",
                    "categoryId": "23"
            }
          }
        )
     response = request.execute()
        

if __name__ == "__main__":
    main()
