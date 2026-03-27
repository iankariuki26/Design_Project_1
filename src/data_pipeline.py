import duckdb
import logging

# Set up logging as per rubric requirement
logging.basicConfig(filename='pipeline.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class MovieLensDB:
    def __init__(self, db_file='movielens.db'):
        try:
            self.con = duckdb.connect(database=db_file)
            logging.info(f"Connected to {db_file}")
        except Exception as e:
            logging.error(f"Failed to connect to database: {e}")
            raise

    def execute_query(self, query):
        try:
            return self.con.execute(query)
        except Exception as e:
            logging.error(f"Query failed: {query[:50]}... Error: {e}")
            return None

    def close(self):
        self.con.close()
        logging.info("Database connection closed.")