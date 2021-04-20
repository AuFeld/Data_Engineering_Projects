class SQLQueries: 
    songplay_table_insert = ("""
        INSERT INTO songplays (playid, start_time, userid, songid, artistid, 
                                sessionid, location, user_agent)
        SELECT
            md5(events.sessionid || events.start_time) songplayid, 
            events.start_time,
            events.userid, 
            events.level, 
            songs.song_id,
            songs.artist_id, 
            events.sessionid, 
            events.location, 
            events.useragent
            FROM (SELECT TIMESTAMP 'epoch' + ts/100 * interval '1 second' AS start_time, *
        FROM staging_events
        WHERE page="NextSong') events
        LEFT JOIN staging_songs songs
        ON events.song = songs.title
            AND events.artist = songs.artist_name
            AND events.length = songs.duration
    """)

    user_table_insert = ("""
        INSERT INTO users (userid, first_name, last_name, gender, level)
        SELECT distinct userid, firstname, lastname, gender, level
        FROM staging_events
        WHERE page = 'NextSong')
    """)

    sort_table_insert = ("""
        INSERT INTO songs (songid, title, artistid, year, duration)
        SELECT distinct song_id, title, artist_id, year, duration
        FROM staging_songs
    """)

    artist_table_insert = ("""
        INSERT INTO artists (artistid, name, location, latitude, longitude)
        SELECT distinct artist_id, artist_name, artist_location, 
            artist_latitude, artist_longitude
        FROM staging_songs
    """)

    time_table_insert = ("""
        INSERT INTO time (start_time, hour, day, week, month, year, dayofweek)
        SELECT start_time, extract(hour from start_time), 
            extract(day from start_time), extract(wek from start_time),
            extract(dayofweek from start_time)
        FROM songplays
    """)
