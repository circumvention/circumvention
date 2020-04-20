import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import urllib.request
import json 
import gdata
import os

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

    request = youtube.videos().update(
        body={
          "id": "gnPPgX1p5lc",
          "snippet": {
            "title": "if this video has views, you're cool"
          }
        }
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()
