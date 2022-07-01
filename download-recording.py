
import requests 
import os
from secrets import ZOOM_ACCESS_TOKEN


def download_Zoom_Recording_Locally(zoom_access_token, download_url):
    new_download_url = download_url +'?access_token=' + zoom_access_token
    
    try:
        response = requests.get(new_download_url, stream=True)
    except requests.exceptions.ConnectionError as err:
        print(err)
        response = requests.get(new_download_url, stream=True)
    try:
        with open("test_download.mp4", 'wb') as videoData:
            for chunk in response.iter_content(chunk_size=1024 * 8):
                if chunk:
                    videoData.write(chunk)
                    videoData.flush()
                    os.fsync(videoData.fileno())
    except Exception as e:
        print(e)
    return "Success"

if __name__ == '__main__':
    ZOOM_ACCESS_TOKEN = "YOUR ACCESS TOKEN"
    download_url = "Meeting Download URL"
   
    print(download_Zoom_Recording_Locally(ZOOM_ACCESS_TOKEN, download_url))



