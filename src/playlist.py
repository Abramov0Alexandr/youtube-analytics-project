import os
import datetime
import isodate
from googleapiclient.discovery import build


class PlayList:
    __API_KEY: str = os.getenv('API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__API_KEY)

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.__playlists_info = self.__youtube.playlists().list(id=playlist_id, part='contentDetails,snippet',
                                                                maxResults=50, ).execute()
        self.__title = self.__playlists_info['items'][0]['snippet']['title']
        self.__url = f"https://www.youtube.com/playlist?list={self.__playlist_id}"

    @property
    def title(self):
        return self.__title

    @property
    def url(self):
        return self.__url

    @property
    def total_duration(self):
        total_duration = datetime.timedelta()
        each_video_info = self.__youtube.playlistItems().list(playlistId=self.__playlist_id, part='contentDetails',
                                                              maxResults=50,).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in each_video_info['items']]

        video_response = self.__youtube.videos().list(part='contentDetails,statistics', id=','.join(video_ids)
                                                      ).execute()

        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration
