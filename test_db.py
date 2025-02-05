import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

try:
    # Create connection using psycopg with binary protocol and connection pooling
    conn = psycopg.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        connect_timeout=3,
        autocommit=True,  # Added for convenience
        options="-c search_path=public"
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}") 