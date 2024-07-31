import sqlite3


def connect():
    connection = sqlite3.connect("mydb.db")
    cursor=connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS data (author TEXT, title TEXT,location TEXT, genre TEXT)""")
    connection.commit()
    connection.close()





def insert(author,title,location,genre):
    connection = sqlite3.connect("mydb.db")
    cursor=connection.cursor()
    cursor.execute(" INSERT INTO data VALUES (?,?,?,?)",(author,title,location,genre))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("mydb.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM data")
    rows=cursor.fetchall()
    connection.close()
    return rows

def search(author="",title="",location="",genre=""):
    connection = sqlite3.connect("mydb.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM data WHERE author=? or title=? or location=? or genre=?",(author,title,location,genre))
    rows=cursor.fetchall()
    connection.close()
    return rows


def delete(title):
    connection = sqlite3.connect("mydb.db")
    cursor=connection.cursor()
    cursor.execute(f'''DELETE FROM data WHERE title="{title}"''')
    connection.commit()
    connection.close()

def update(author,title,location,genre):
    connection = sqlite3.connect("mydb.db")
    cursor=connection.cursor()
    cursor.execute("UPDATE data SET author=? , title=? , location=? , genre=? WHERE id=? ",(author,title,location,genre))
    connection.commit()
    connection.close()
connect()
#insert("charles dickens","jane eyre","sixth row","classics")
#insert("shakespeare","pride and prejudice","forth row","classics")
#insert("wael","mahmoud",6,4)
#update(1,"sherif","said",10,3.8)
#print(search(fn="sherif"))
#delete(tuple[title])
print(view())


