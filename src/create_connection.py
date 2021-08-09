from sqlalchemy import create_engine
import os

class CreateConnection:

    def __init__(self):
        self.engine = create_engine(os.getenv("REPO_URL"))
        self.connection = self.engine.connect()
    
    def close_connection(self):
        self.connection.close()
