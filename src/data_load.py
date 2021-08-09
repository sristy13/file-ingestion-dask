from dask import dataframe as dd
import os
from src.create_connection import CreateConnection
from src.create_client import CreateClient
from loginit import AppLogger


def load():
    
    try:
        # create dask client
        client = CreateClient()

        # read csv file
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","files",os.getenv("CSV_NAME"))
        dask_df = dd.read_csv(file_path)

        # create temp table and load csv data to temp table
        dask_df.to_sql(
            os.getenv("TEMP_TABLE"),
            os.getenv("REPO_URL"),
            if_exists="replace",
            index=False,
            chunksize=10000,
            parallel=True)

        # create connection to target database
        conn = CreateConnection()

        # delete records from target table which is present in temp table identified using sku
        conn.connection.execute("delete from {} where sku in (select sku from {})".format(
            os.getenv("TARGET_TABLE"),os.getenv("TEMP_TABLE")))
        
        # insert data to target table. Existing records will get updated as first delete then insert is taking place
        dask_df.to_sql(
            os.getenv("TARGET_TABLE"),
            os.getenv("REPO_URL"),
            if_exists="append",
            index=False,
            chunksize=10000,
            parallel=True)

        # drop temp table
        conn.connection.execute("drop table {}".format(os.getenv("TEMP_TABLE")))

        # perform aggregation to find number of products having same name and save to aggregated table
        conn.connection.execute("insert into {} (select name,count(name) as number_of_products from {} group by name)".format(
            os.getenv("AGG_TABLE"),os.getenv("TARGET_TABLE")
        ))
        conn.close_connection()


    except Exception as ex:
        AppLogger.error("Failed to perform data ingestion. Error: "+str(ex))
