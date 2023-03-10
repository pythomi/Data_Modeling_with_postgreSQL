# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time bigint NOT NULL,
    user_id int NOT NULL,
    level varchar,
    song_id varchar,
    artist_id varchar,
    session_id int,
    location varchar,
    user_agent varchar)
    """)


user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
user_id int PRIMARY KEY,
first_name varchar,
last_name varchar,
gender varchar(1),
level varchar)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
song_id varchar PRIMARY KEY,
title varchar NOT NULL,
artist_id varchar NOT NULL,
year int,
duration float)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
artist_id varchar PRIMARY KEY,
name varchar NOT NULL,
location varchar,
latitude float,
longitude float)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
start_time bigint PRIMARY KEY,
hour int,
day int,
week int,
month int,
year int,
weekday int)
""")

# INSERT RECORDS (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)

songplay_table_insert = ("""INSERT INTO songplays (
    songplay_id,
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent)
    VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
    """)


user_table_insert = ("""INSERT INTO users (
user_id,
first_name,
last_name,
gender,
level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""INSERT INTO songs (
song_id,
title,
artist_id,
year,
duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""INSERT INTO artists (
artist_id,
name,
location,
latitude,
longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")


time_table_insert = ("""INSERT INTO time (
start_time,
hour,
day,
week,
month,
year,
weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

# FIND SONGS
### FROM etl.ipynb: cur.execute(song_select, (row.song, row.artist, row.length))
song_select = ("""SELECT st.song_id, at.artist_id
FROM songs st
JOIN artists at
ON st.artist_id = at.artist_id
WHERE st.title = %s AND at.artist_id = %s AND st.duration = %s

""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
