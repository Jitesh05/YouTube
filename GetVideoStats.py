
def get_video_stats_by_id(youtube, video_id):
    request = youtube.videos().list(part="snippet, statistics", id=video_id)
    response = request.execute()
    return response


