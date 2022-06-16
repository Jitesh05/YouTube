import json
from FlattenJSON import flatten_json
from pandas import json_normalize


def get_channel_stats_by_id(youtube, channel_id):
    request = youtube.channels().list(part="snippet, statistics", id=channel_id)
    response = request.execute()
    print(type(response))
    return response


def clean_channel_stats(self):
    channel_id = (self['items'][0]['id'])
    channel_name = (self['items'][0]['snippet']['title'])
    channel_country = (self['items'][0]['snippet']['country'])
    channel_stats = (self['items'][0]['statistics'])
    views = channel_stats['viewCount']
    subscribers = channel_stats['subscriberCount']
    videos = channel_stats['videoCount']

    return [channel_id, channel_name, channel_country, views, subscribers, videos]
