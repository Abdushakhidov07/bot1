from connection import connection





async def get_user(telegram_id):
    try:
        conn = await connection()
        users = await conn.fetchrow("""
        select * from users where telegram_id = $1                           
        """, str(telegram_id))
        return users
    except Exception as error:
        print(f"Error in get users: {error}")
    finally:
        await conn.close()
        
async def save_user(telegram_id, username, firstname, lastname):
    try:
        conn = await connection()
        await conn.execute("""
        INSERT INTO users(telegram_id, username, full_name) VALUES
        ($1, $2, $3)
        """, str(telegram_id), username, firstname)
        print("User saved")
    except Exception as error:
        print(f"Error in save users: {error}")
    finally:
        await conn.close()
        

async def get_all_user():
    try:
        conn = await connection()
        users = await conn.fetch("""
        select * from users                          
        """)
        return users
    except Exception as error:
        print(f"Error in get all users: {error}")
    finally:
        await conn.close()
        