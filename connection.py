import asyncpg
import os
from dotenv import load_dotenv


load_dotenv()
ps = os.getenv("PASSWORD_DB")



async def connection():
    try:
        conn = await asyncpg.connect(
            database="bot2_db",
            host="localhost",
            user = "postgres",
            port = 5432,
            password=ps
        )
        print("Connection OK")
        return conn
    except Exception as error:
        print(f"Connection Error: {error}")
        

async def create_table():
    conn = await connection()
    try:
        await conn.execute("""
     CREATE TABLE IF NOT EXISTS users( 
                   user_id serial primary key,
                   username varchar(100),
                   full_name varchar(100),
                   telegram_id varchar,
                   created_at timestamp DEFAULT NOW(),
                   is_active boolean DEFAULT true
                   ); 
                """)
        print("Table created!")
    except Exception as error:
        print(f"Create table Error: {error}")
    finally:
        await conn.close()