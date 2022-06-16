import pyodbc


def insert_into_staging(channel_stats, cursor):

    channel_stats_list = channel_stats
    var_string = ', '.join('?' * len(channel_stats_list))
    insert_script = 'INSERT INTO [dbo].[YT_Channel_Stats] (Channel_ID, Channel_Name, Country, Views, Subscribers, Videos)' \
                    'VALUES (%s);' % var_string

    cursor.execute(insert_script, channel_stats_list)
    cursor.commit()

