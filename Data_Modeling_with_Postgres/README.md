
# Data Modeling with Postgres

## **Overview**
In this project, I applied Data Modeling with Postgres and built an ETL pipeline using Python. A startup wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. Currently, they are collecting data in H5 format and the analytics team is particularly interested in understanding what songs users are listening to.


## **Song Dataset**
Songs dataset is a subset of [Million Song Dataset](http://millionsongdataset.com/).

Sample Record :
```
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

## Schema

#### Fact Table 
**songplays** - records in log data associated with song plays i.e. records with page `NextSong`

```
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
```

#### Dimension Tables
**users**  - users in the app
```
user_id, first_name, last_name, gender, level
```
**songs**  - songs in music database
```
song_id, title, artist_id, year, duration
```
**artists**  - artists in music database
```
artist_id, name, location, latitude, longitude
```
**time**  - timestamps of records in  **songplays**  broken down into specific units
```
start_time, hour, day, week, month, year, weekday
```

## Project Files

```sql_queries.py``` contains sql queries for dropping and  creating fact and dimension tables. Also, contains insertion query template.

```create_tables.py``` contains code for setting up database. Running this file creates **sparkifydb** and also creates the fact and dimension tables.

```etl.py``` will read and process **song_data**

## Environment 
Python 3.9 or above

PostgresSQL 9.5 or above

psycopg2 - PostgreSQL database adapter for Python


## How to run

Run the drive program ```main.py``` as below.
```
python main.py
``` 

The ```create_tables.py``` and ```etl.py``` file can also be run independently as below:
```
python create_tables.py 
python etl.py 
```

#### Data Model

[DE 1 Data Model](/images/de1_data_model.png)

#### Reference: 
[Psycopg](http://initd.org/psycopg/docs/)

[PostgreSQL Documentation](https://www.postgresql.org/docs/)

[Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)

