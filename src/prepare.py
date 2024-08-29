
def start_preperation():
    from sqlite3 import connect
    connection = connect("src/officelens_data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='categories'")
    if cursor.fetchone() is None:
        cursor.execute("CREATE TABLE categories (id INTEGER PRIMARY KEY, name TEXT, color TEXT, tag TEXT)")
        connection.commit()
        print("[DEBUG] Created table categories.")

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='entries'")
    if cursor.fetchone() is None:
        cursor.execute("CREATE TABLE entries (id INTEGER PRIMARY KEY, title TEXT, category TEXT, date INTEGER, amount REAL, description TEXT)")
        connection.commit()
        print("[DEBUG] Created table entries.")
    connection.close()

    print("[DEBUG] Finished preperation.")