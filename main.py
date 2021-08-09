from dotenv import load_dotenv
import datetime
from src.data_load import load
from loginit import AppLogger

try:
    load_dotenv()
except Exception as ex:
    AppLogger.error("Failed to load env file. Error: "+str(ex))
    raise(ex)

start = datetime.datetime.now()
AppLogger.info("Data Ingestion is started.")
load()
AppLogger.info("Time taken for data ingestion is {}".format(str(datetime.datetime.now()-start)))
