import googleapiclient.discovery  # API client library
from GetVideoStats import get_video_stats_by_id
from GetChannelStats import get_channel_stats_by_id, clean_channel_stats
from FlattenJSON import flatten_json
from pandas import json_normalize
import json
from InsertIntoStaging import insert_into_staging
from ReCreateDBOjects import recreate_stg_tables

#method for creating new staging table with every run
# retunrs a cursor object whcih can be used later to insert data into the table
cursor = recreate_stg_tables()

#list of channel ids. to be provided manually
channel_ids = ['UCVE3f6KA6N56xW4m9i662yw', 'UCQVBwcAEuqVumhctTCnd0Nw', 'UCllSh_d1Brc9PLypjhm1_YA']

# API information
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
DEVELOPER_KEY = 'AIzaSyCP0sgs8K51N3YDtxiYJ_0wYHUXrrE9rUU'

youtube = googleapiclient.discovery.build(API_SERVICE_NAME,
                                          API_VERSION,
                                          developerKey=DEVELOPER_KEY)

for channel_id in channel_ids:
    try:
        channel_stats_response = get_channel_stats_by_id(youtube, channel_id)
        channel_stats_list = clean_channel_stats(channel_stats_response)
        insert_into_staging(channel_stats_list, cursor)
        print(channel_id + " Inserted Successfully")
    except:
        print('Error Occurred for Channel ID: ' + channel_id)

cursor.close()