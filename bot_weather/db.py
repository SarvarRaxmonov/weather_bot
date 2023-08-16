import sqlite3

conn = sqlite3.connect("bot.db" ,check_same_thread=False)
cursor = conn.cursor()
def update_or_insert_data(data, user):
    if user:
        cursor.execute(f"UPDATE user_id SET location = ? WHERE user_id = ?", (data,user))
    else:
        cursor.execute(f"INSERT INTO user_id (user_id,location) VALUES (?,?)", (data[0],data[1]))
    conn.commit()

def user_exists(user_id):
    cursor.execute(f"SELECT * FROM user_id WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    return user is not None

def get_location_of_user(user_id):
    cursor.execute(f"SELECT location FROM user_id WHERE user_id = ?", (user_id,))
    location = cursor.fetchone()[0]
    return location
