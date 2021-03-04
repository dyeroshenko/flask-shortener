import sqlite3

connector = sqlite3.connect('url.db')
cursor = connector.cursor()

# cursor.execute("""
#     CREATE TABLE urls (
#         id INTEGER PRIMARY KEY,
#         hashed_id TEXT NOT NULL,
#         timestamp_CET TEXT NOT NULL,
#         full_url TEXT NOT NULL, 
#         domain TEXT NOT NULL,
#         visits INTEGER NOT NULL
#         )
#     """)

# cursor.execute("""
#             INSERT INTO urls (id, hashed_id, timestamp_CET, full_url, domain, visits) 
#             VALUES (1, '3W', '04/03/2021 09:08:15', 'https://github.com/dyeroshenko', 'github.com', 0)
# """)


cursor.execute("SELECT * FROM urls")
x = cursor.fetchall()

connector.commit()
connector.close()

print(x)
