#Opens a connection to your PostgreSQL database when the spider starts.
#Inserts each scraped item (your JSON data) into a table.
#Closes the connection when the spider finishes.

#In the open_spider method, use psycopg2.connect(...) to connect to your database. Use your connection credentials (for local testing, these will be similar to those you provided when running Docker).
#Use the environment variables for the .env file to connect to the database.


import os
import psycopg
from typing import Dict, Any
from scrapy import Spider
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

class PostgresPipeline:
    def open_spider(self, spider: Spider):
        """Connect using environment variables"""
        try:
            self.connection = psycopg.connect(
                dbname=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host=os.getenv("POSTGRES_HOST"),
                port=os.getenv("POSTGRES_PORT", "5432")
            )

            self.cursor = self.connection.cursor()
            spider.logger.info("Connected to PostgreSQL successfully")
        except Exception as e:
            spider.logger.error(f"Connection failed: {e}")
            raise

    def close_spider(self, spider: Spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item: Dict[str, Any], spider: Spider) -> Dict[str, Any]:
        try:
            self.cursor.execute(
                "INSERT INTO json_ld (data) VALUES (%s)",
                (dict(item),)
            )
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            spider.logger.error(f"Insert failed: {e}")
        return item

