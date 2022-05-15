import sqlite3

def CreateTable():
    try:
        sqlite_connection = sqlite3.connect("reviews.db")
        cursor = sqlite_connection.cursor()
        print('База данных sqlite успешно создана и подключена')
        
        sqlite_create_table_query = '''CREATE TABLE reviews(
            id INTEGER PRIMARY KEY,
            review TEXT NOT NULL);'''
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблица успешно создана")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с SQLite возникла ошибка: ", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")

def getMaxID() -> int:
    try:
        sqlite_connection = sqlite3.connect("reviews.db")
        cursor = sqlite_connection.cursor()
        select_query = "SELECT MAX(id) FROM reviews"
        
        cursor.execute(select_query)
        record = cursor.fetchone()
        
        if record[0] == None:
            return 0
        return record[0]
    except sqlite3.Error as error:
        print("Error:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            
def addreview(something):
    try:
        sqlite_connection = sqlite3.connect("reviews.db")
        cursor = sqlite_connection.cursor()
        
        insert_query = '''INSERT INTO reviews (id, review)
        VALUES (?, ?);'''
        
        cursor.execute(insert_query, (getMaxID() + 1, something,))
        sqlite_connection.commit()
        
        cursor.close()
    except sqlite3.Error as error:
        print("Error: ", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
def addreview2(id, something):
    try:
        sqlite_connection = sqlite3.connect("reviews.db")
        cursor = sqlite_connection.cursor()
        
        insert_query = '''INSERT INTO reviews (id, review)
        VALUES (?, ?);'''
        
        cursor.execute(insert_query, (id, something,))
        sqlite_connection.commit()
        
        cursor.close()
    except sqlite3.Error as error:
        print("Error: ", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            
def GetTable():
    try:
        sqlite_connection = sqlite3.connect("reviews.db")
        cursor = sqlite_connection.cursor()
        sqlite_select_query = "SELECT * FROM reviews;"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с SQLite возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
CreateTable()