# Data_Modeling_with_postgreSQL
# THE SPARKIFYDB DATABASE

Here you can evaluate song datas and log files from the 'Next Song' website.

The data is made available in 5 different SQL tables.
The table are arranged in Star Schema:

#### 1 Fact Table
- songplays

#### 4 Dimension Tables
- users
- songs
- artists
- time



To do this, follow these steps:
1. To create the tables, run "create_tables.py"
  - connects to the sparkifydb and create the tables from sql_queries.py file
2. To fill the tables with the data, run "etl.py"
  - reads the folders and subfolders data/log_data and data/song_data

Now SQL queries can be executed for the 5 tables in the sparkifydb.
