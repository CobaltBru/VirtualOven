from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import webview
import time

DEVELOPER_KEY = "AIzaSyDCFteWNIVFwSwOp0Mdz410jdGcoaSqcUM" #유튜브 API 키 값
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)


if __name__ == '__main__':
    window = webview.create_window('Woah dude!', 'https://youtu.be/w3fCsb4pgps?t=302')
    webview.start()


