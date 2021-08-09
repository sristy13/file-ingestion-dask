import logging
import os


CHECK_LOG_DIR = os.path.isdir(os.path.join(os.getcwd(),"log"))
if not CHECK_LOG_DIR:
    os.makedirs(os.path.join(os.getcwd(),"log"))

def getLoggerInstance(name,fileName):

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(
        os.path.join(os.getcwd(),"log",fileName),"a"
    )
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

AppLogger = getLoggerInstance("application","app.log")