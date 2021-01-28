# Project 1 Data Modeling with Postgres


### I. Project purpose
This project consist to create a Postgres database and define an etl pipline to get data from differents JSON logs files for insert into this database created.
The goal of this project is to provide to the analytics team of an startup called Sparkify a systems that permit their to anlyse their users'activites and to optimise their queries on the data.

### II. Database Schema
Sparkify activity is the music streaming. So the database the structure is composed to five tables:
* Four Dimension tables which contains all details on each entity of music streaming activity
* One Fact table that permit to the team to optimse their queries and to do their analysticx easily.
### 1. Dimension Tables
These tables was create for respect the normalisation concept. Each of these tables has a primary key  column that can be used to find all other columns. 

### a.  Users: 
This table contains all details about the users which played a song
>   user_id varchar PRIMARY KEY,\
    first_name varchar ,\
    last_name varchar,\
    gender varchar,\
    level varchar NOT NULL); 

### b. songs : 
This table contains all details of the diffrents songs played
> song_id VARCHAR PRIMARY KEY,\
  title VARCHAR,\
  artist_id VARCHAR NOT NULL,\
  year INT,\
  duration DECIMAL
  
 ### c. artists : 
 This table contains all details about the differents artists that their are songs available on the music plateforme
 > artist_id VARCHAR PRIMARY KEY,\
   name VARCHAR,\
   location VARCHAR NOT NULL,\
   latitude VARCHAR,\
   longitude VARCHAR
   
 ### b. times : 
 This table is the temporal dimension. It give us when the song was played
> start_time VARCHAR PRIMARY KEY,\
  hour INT,\
  day INT,\
  week INT,\
  month INT,\
  year INT,\
  weekday INT


### 2. Fact Table

 ### a. Songsplays:
 This is the fact table it don't respect the normalisation concept but it'll permit to the analysts team to do easy queries and very quickly.
 We defined more REFERENCES and NOT NULL constraint on those columns to for make a reference to each dim tables 
 
 > songplay_id SERIAL PRIMARY KEY,\
   start_time varchar REFERENCES times,\
   user_id varchar REFERENCES users,\
   song_id varchar REFERENCES songs,\
   artist_id varchar REFERENCES artists,\
   level varchar NOT NULL,\
   session_id int NOT NULL,\
   location varchar NOT NULL,\
   user_agent varchar NOT NULL
 

### II. ETL SCRIPT
As we mentioned in project description section the project consist to create a database and get the data form differents JSON logs files and insert into the database. So we have to define in our ETL Script how process these actions.

1. First we have a function that browse the different log paths to get each songs and artists json file and fit it in different "pandas dataframe".

2. After we extract from each dataframe the differents colunms that corresponded to our differents tables columns (e.g: for artist table, we extract from the log file artist_id name, location, latitude, longitude) and pass these informations to another function that execute a query to insert into the database tables.

3. Third, we Browse another log path called songs_file that contains the differents users activities and fit each json file to dataframe and take differents information about the users and the time that they played music to insert into the differents tables throuht another function.

4. Finally, we make a select query on artists and songs tables by the user_id to get the differents rows are matched and we complete these information with others information that we extrat form the songs_file log file to insert into the songsplays table of our database. 

### III. EXAMPLE OF QUERIES 

1. Get how many times the users played each songs of artist_id which id is 'ARD7TVE1187B99BFB1'

> SELECT COUNT(song_id), song_id FROM songsplays
  WHERE artist_id='ARD7TVE1187B99BFB1' 
  GROUP BY song_id
  
2. Get differents artists that their song was played by the users

> SELECT DISTINCT(artsit_id) FROM songplays

 ### IV. FILES DECRIPTION
 The project composed to for mains files and two files supplementary for test to tests.
 
1. Mains Files:
        * sql_queries.py : In this this file we writed queries to cerate tables, Drop tables and insert into these table
        * create_tables.py:  This file contains the functions that execute queries that permit to drop and create the differents tables of the database.
        * etl.py:  This script this script browses all the 'song_data' and 'log_data'
            folders in the data directory in order to insert the different data into the
            different tables created.

2. Test Files:
        * test.ipynb: This notebook is due to testing purpose. It contains simple requests to visualize saved data.
        * etl.ipynb: This is another notebook that permit to us to test our differents functions before to pass to the etl.py.


3. How Does works
  * Firstly run into a console the create_tables.py file
  * Secondly run the etl.py file 
 #Note: If you used the test.ipynb or etl.ipynb, before run the create_tables.py, make sure that you are restart the different kernel for close the database connection.

4. Readme.md File: This is this file we explains the project purpose and give the differents steps we followed to realise this project.



### V. EXECUTION SCREEN SHOT


1. A song_data json file to pandas Dataframe 
![Screen shot 1](https://i.imgur.com/Jgu7mhd.png)

2. Some rows inserted into songsplays table
![Screen shot 2](https://i.imgur.com/X06z1EN.png)

3. Run etl.py
![Screen shot 3](https://i.imgur.com/QRoSWJZ.png)
 
 
 
 
 