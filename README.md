# Data Engineering Projects

Data Modeling, Data Pipelines wtih Airflow, Data Lakes, Infrastructure setup on AWS, Data Warehousing, Pipeline Monitoring, and Pipeline Alerts

![architecture](/images/architecture.png)

## Project 1: Data Modeling with Postgres
In this project, I applied Data Modeling with Postgres and built an ETL pipeline using Python. A startup wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. Currently, the start up is collecting data in H5 format and the analytics team is particularly interested in understanding what songs users are listening to.

Link: [Data Modeling with Postgres](https://github.com/AuFeld/Data_Engineering_Projects/tree/main/Data_Modeling_with_Postgres)

## Project 2: Data Modeling with Cassandra
In this project, I applied Data Modeling with Cassandra and constructed an ETL pipeline via Python. A Data Model was constructed based on the queries to address the following:
1. Get details of a song that was heard on the music app history during a particul session
2. Get songs played by a user during a particular session on the music app
3. Get all users from the music app history who listened to a particular song

Link: [Data Modeling with Cassandra](https://github.com/AuFeld/Data_Engineering_Projects/tree/main/Data_Modeling_with_Cassandra)

## Project 3: Data Warehouse on AWS
In this project, I constructed a Data Warehouse on AWS and engineered an ETL pipeline to extract and transform data stored in the S3 buckets and migrated data to the Data Warehouse hosted on Amazon Redshift. 

Using Redshift IaC script - [Redshift_IaC_README](https://github.com/AuFeld/Data_Engineering_Projects/blob/master/Redshift_IaC_README.md)
Link: [Data_Warehouse](https://github.com/AuFeld/Data_Engineering_Projects/tree/master/Data_Warehouse)

## Project 4: Data Lake
In this project, I will build a Data Lake on AWS using Spark and AWS EMR cluster. The data lake will be the single source for the analytics platform. Utilizing spark jobs to perform ELT operations that picks data from the S3 landing zone, then transforming and storing data on the S3 processed zone.

Link: **COMING SOON!**