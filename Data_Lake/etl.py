import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, monotonically_increasing_id
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format, dayofweek
from pyspark.sql.types import *

config = configparser.ConfigParser()
config.read("dl.cfg")

os.environ["AWS_ACCESS_KEY_ID"] = config["AWS_ACCESS_KEY_ID"]
os.environ["AWS_ACCESS_KEY_ID"] = config["AWS_SECRET_ACCESS_KEY"]

def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return Spark 

def process_song_data(spark, input_data, output_data):
    """
    Process the songs data files and create extract songs table and artist data
    from it. 

    :param spark: a spark session instance
    :param input_data: input file path
    :param output_data: output file path
    """

    # get filepath to song data file
    song_data = input_data + "song_data/*/*/*/*"

    # read song data file
    df = spark.read.json(log_data, mode="PERMISSIVE", 
                        columnNameOfCorruptRecord="corrupt_record").drop_duplicates()
    
    # filter by actions from song plays
    df = df.filter(df.page == "NextSong")

    # extract columns for users table
    users_table = df.select("userId","firstName","lastName","gender",
                            "level").drop_duplicates()
    
    # write users table to parquet files
    users_table.write.parquet(os.path.join(output_data, "users/") , 
                                mode="overwrite")
    
    # create timestamp column from original timestamp column
    get_timestamp = udf(lambda x : datetime.utcfromtimestamp(int(x)/1000, 
                            TimestampType())
    df =  df.withColumn("start_time", get_timestamp("ts"))

    # extract columns to create time table
    time_table = df.withColumn("hour",hour("start_time"))\
                    .withColumn("day",dayofmonth("start_time"))\
                    .withColumn("week",weekofyear("start_time"))\
                    .withColumn("month",month("start_time"))\
                    .withColumn("year",year("start_time"))\
                    .withColumn("weekday",dayofweek("start_time"))\
                    .select("ts", "start_time","hour","day","week","month",
                            "year","weekday").drop_duplicates() 
    
    # write time table to parquet files partioned by year and month
    time_table.write.parquet(os.path.join(output_data, "time_table/"), 
                                mode="overwrite", 
                                partitionBy=["year","month"])
    
    # read in song data to use for songplays table
    song_df = spark.read\
                .format("parquet")\
                .option("basePath", os.path.join(output_data, "songs/"))\
                .load(os.path.join(output_data, "songs/*/*/"))
    
    # extract columns from joined song and log datasets to cerate songplays table
    songplays_table = df.join(song_df, df.song == song_df.title, how="inner")\
                        .select(monotonically_increasing_id().alias("songplay_id"), 
                                col("userId").alias("user_id"),"level", 
                                "song_id","artist_id", 
                                col("sessionId").alias("session_id"), 
                                "location",
                                col("userAgent").alias("user_agent"))
    
    songplays_table = songplays_table.join(time_table, 
                                            songplays_table.start_time, 
                                            how="inner")\
                        .select("songplay_id", songplays_table.start_time, 
                                "user_id","level","song_id","artist_id", 
                                "session_id","location","user_agent", "year",
                                "month")
    
    # write songplays table to parquet files partioned by year and month
    songplays_table.drop_duplicates().write.parquet(os.path.join(output_data, 
                                                    "songplays/"), 
                                                    mode="overwrite", 
                                                    partionBy=["year","month"])
    
    def main():
        spark = create_spark_session()
        input_data = "s3://udacity-spark-project/"
        output_data= "s3://udacity-spark-project/output/"

        process_song_data(spark, input_data, output_data)
        process_log_data(spark, input_data, output_data)

    if__name__ == "__main__":
        main()

