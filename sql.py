import sqlite3
 
conn = sqlite3.connect("mydatabase.db")
#conn.row_factory = sqlite3.Row
cursor = conn.cursor()

def create_table():
    try:
        conn = sqlite3.connect('SQLite.db')  
        curs = conn.cursor() 

        curs.execute('''CREATE TABLE IF NOT EXISTS Table_2
             ([id] INTEGER PRIMARY KEY AUTOINCREMENT , [name] text, [email] text, [joining_date] date, [salary] integer)''')
 
        conn.commit()

        conn.close()

    except sqlite3.Error as e:
        print(str(e))


create_table()


'''cursor.execute("""INSERT INTO albums
                  VALUES ('Glow', 'Andy Hunter', '7/24/2012',
                  'Xplore Records', 'MP3')"""
               )
 
# Сохраняем изменения
conn.commit()


sql = "SELECT * FROM albums"
cursor.execute(sql)
print(cursor.fetchall())


conn.close()
'''
