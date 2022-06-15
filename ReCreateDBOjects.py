import pyodbc


def recreate_stg_tables():
    server = 'ral-bi-devsql'
    database = 'ItronStaging'

    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE [dbo].[YT_Channel_Stats]''')
    cursor.execute('''
                   CREATE TABLE [dbo].[YT_Channel_Stats] (
                            Channel_ID varchar(100),
                            Channel_Name varchar(255),
                            Country varchar(20),
                            [Views] int,
                            Subscribers int,
                            Videos int
                        )
    ''')
    conn.commit()
    return cursor