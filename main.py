from dotenv import load_dotenv
import datetime
from src.data_load import load
from loginit import AppLogger

# load env file
try:
    load_dotenv()
except Exception as ex:
    AppLogger.error("Failed to load env file. Error: "+str(ex))
    raise(ex)

# driver code
start = datetime.datetime.now()
AppLogger.info("Data Ingestion is started.")
# call data ingestion function
load()
AppLogger.info("Time taken for data ingestion is {}".format(str(datetime.datetime.now()-start)))
