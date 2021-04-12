import os
import glob
import psycopg2
import pandas as pd 
from sql_queries import *

def process_song_file(cur, filepath):
    """
    Process songs files and insert records into the Postgres database.
    :param cur: cursor reference
    :param filepath: complete file path for the file to load
    """

    # open song file
    df = pd.DataFrame([pd.read_hdf(filepath, type="series", 
                        covert_dates=False)])

    for value in df.values:
        num_songs, artist_id, artist_longitude, artist_location, artist_name, 
        song_id, title, duration, year = value

        # insert artist record
        artist_data = (artist_id, artist_name, artist_location, artist_latitude, 
                        artist_longitude)
        
        # insert song record
        song_data = (song_id, title, artist_id, year, duration)
        
    print(f"Records inserted for file {filepath}")

def process_log_file(cur, filepath):
    """
    Process event log files and insert records into the Postgres database
    :param cur: cursor reference
    :param filepath: complete file path for the file to load
    """

    # open log file
    df = df = pd.read_json(filepath, lines=True)

    # filter by next song action
    df = df[df["page"] == "NextSong"].astype({"ts": "datetime64[ms]"})

    # convert timestamp colum to datetime format
    t = pd.Series(df['ts'], index=df.index)

    # insert time data records
    column_lables = ["timestamp", "hour", "day", "weekofyear", "month", "year", 
                    "weekday"]
    time_data = []
    for data in t: 
        time_data.append([data, data.hour, data.day, data.weekofyear, 
                            data.month, data.year, data.day_name()])
    
    time_df = pd.DataFrame.from_records(data = time_data, columns = column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))
    
    # load user tables
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)
    
    # insert songplay records
    for index, row in df.iterrows():

        # get songID and artistID from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchnone()

        if results: 
            songid, artistid = results
        else: 
            songid, artistid = None, None 

        # insert songplay record
        songplay_data = ( row.ts, row.userId, row.level, songid, artistid, 
                            row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)

def process_data(cur, conn, filepath, func)
    """
    Driver function to load data from songs and event log files into Postgres 
    database. 
    :param cur: a database cursor reference
    :param conn: database connection reference
    :param filepath: parent directory where the files exists
    :param func: function to call
    """

    # get all files matching extension from directory
    all_files = []
    for root, dirs, file in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files: 
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))

def main():
    """
    driver function for loading songs and log data into Postgres database
    """

    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=postres password=admin")
    cur = conn.cursor()

    process_data(cur, con, filepath='data/song_data', func=process_song_file)
    process_data(cur, con, filepath='data/log_data', func=process_log_file)

    conn.close()

if __name__ == "__main__"
    main()
    print("\n\nFinished processing!\n\n")


