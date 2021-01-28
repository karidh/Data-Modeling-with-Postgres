# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songsplays"
user_table_drop = "DROP TABLE IF EXISTS  users"
song_table_drop = "DROP TABLE IF EXISTS  songs"
artist_table_drop = "DROP TABLE IF EXISTS  artists"
time_table_drop = "DROP TABLE IF EXISTS  times"

# CREATE TABLES

""" Create songsplays table if the table does not exist """
songplay_table_create = ("CREATE TABLE IF NOT EXISTS songsplays(songplay_id SERIAL PRIMARY KEY,\
                                                                start_time varchar REFERENCES times,\
                                                                user_id varchar REFERENCES users,\
                                                                song_id varchar REFERENCES songs,\
                                                                artist_id varchar REFERENCES artists,\
                                                                level varchar NOT NULL,\
                                                                session_id int NOT NULL,\
                                                                location varchar NOT NULL,\
                                                                user_agent varchar NOT NULL);\
                                                                ")


"""
    Create the dim table users if the table does not exist
"""
user_table_create = ("CREATE TABLE IF NOT EXISTS users(user_id varchar PRIMARY KEY,\
                                                      first_name varchar ,\
                                                      last_name varchar,\
                                                      gender varchar,\
                                                      level varchar NOT NULL);\
                                                      ")
"""
    Create the dim table songs if the table does not exist
"""
song_table_create = ("CREATE TABLE IF NOT EXISTS songs(song_id varchar PRIMARY KEY,\
                                                       title varchar,\
                                                       artist_id varchar NOT NULL,\
                                                       year int,\
                                                       duration decimal);")

"""
Create the dim table artist if the table does not exist
"""
artist_table_create = ("CREATE TABLE IF NOT EXISTS artists(artist_id varchar PRIMARY KEY,\
                                                            name varchar,\
                                                            location varchar NOT NULL,\
                                                            latitude varchar,\
                                                            longitude varchar);\
                                                            ")


"""
    Create the dim table times if the table does not exist
"""
time_table_create = ("CREATE TABLE IF NOT EXISTS times(start_time varchar PRIMARY KEY,\
                                                       hour int,\
                                                       day int,\
                                                       week int,\
                                                       month int,\
                                                       year int,\
                                                       weekday int);\
                                                       ")





# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songsplays(start_time , user_id , level , song_id, artist_id,session_id ,location,user_agent) \
                          VALUES(%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING")

user_table_insert = ("INSERT INTO users(user_id, first_name, last_name, gender, level)\
                      VALUES(%s,%s,%s,%s,%s) ON CONFLICT(user_id) DO UPDATE\
                      SET first_name = EXCLUDED.first_name,\
                          last_name = EXCLUDED.last_name,\
                          gender = EXCLUDED.gender,\
                          level = EXCLUDED.level")

song_table_insert = ("INSERT INTO songs(song_id, title, artist_id, year, duration)\
                          VALUES(%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING")

artist_table_insert = ("INSERT INTO artists(artist_id, name , location , latitude , longitude )\
                        VALUES(%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING")


time_table_insert = ("INSERT INTO times(start_time, hour , day , week , month , year , weekday )\
                      VALUES(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING")

# FIND SONGS

song_select = ("SELECT s.song_id, a.artist_id FROM songs s JOIN artists a ON a.artist_id = s.artist_id  WHERE title = %s and name= %s and duration=%s;")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]