
from sqlite3 import connect

def create(title, color, tag):
    connection = connect("src/officelens_data.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO categories (name, color, tag) VALUES (?, ?, ?)", (title, color, tag))
    connection.commit()
    connection.close()
    if cursor.rowcount == 1:
        return True
    else:
        return "Failed to create category."

def get():
    connection = connect("src/officelens_data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM categories")
    response = cursor.fetchall()
    connection.close()
    jsonList = []
    for category in response:
        json = {
            "id": category[0],
            "name": category[1],
            "color": category[2],
            "tag": category[3]
        }
        jsonList.append(json)
    return jsonList

def remove(id):
    connection = connect("src/officelens_data.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM categories WHERE id = ?", (id,))
    connection.commit()
    connection.close()
    if cursor.rowcount == 1:
        return True
    else:
        return "Failed to remove category."