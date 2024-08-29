
from sqlite3 import connect

def create(title: str, category: str, date: int, amount: float, description: str):
    connection = connect("src/officelens_data.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO entries (title, category, date, amount, description) VALUES (?, ?, ?, ?, ?)", (title, category, date, amount, description))
    connection.commit()
    connection.close()
    if cursor.rowcount == 1:
        return True
    else:
        return "Failed to create entry."

def get():
    connection = connect("src/officelens_data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM entries")
    response = cursor.fetchall()
    connection.close()
    jsonList = []
    for entry in response:
        json = {
            "id": entry[0],
            "title": entry[1],
            "category": entry[2],
            "date": entry[3],
            "amount": entry[4],
            "description": entry[5]
        }
        jsonList.append(json)
    return jsonList

def remove(id: int):
    connection = connect("src/officelens_data.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM entries WHERE id = ?", (id,))
    connection.commit()
    connection.close()
    if cursor.rowcount == 1:
        return True
    else:
        return "Failed to remove entry."

def edit(id: int, title: str, category: str, date: int, amount: float, description: str):
    connection = connect("src/officelens_data.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE entries SET title = ?, category = ?, date = ?, amount = ?, description = ? WHERE id = ?", (title, category, date, amount, description, id))
    connection.commit()
    connection.close()
    if cursor.rowcount == 1:
        return True
    else:
        return "Failed to edit entry."