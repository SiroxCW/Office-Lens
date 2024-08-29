
# Office Lens

### Description
You have been tasked with developing a program for a revenue-expense calculator that will allow users to control their finances more effectively. The application should enable users to record their income and expenses and better understand their financial situation through clear and illustrative statistics.

### Components
* C# Winforms UI for building the frontend
* Python for the backend
* SQLite database

#### Communication
* The frontend communicates with the backend via HTTP requests which are handled by Python Flask

### Features (requested by the customer):
* Creation of billing entries 
  - Amount in EUR
  - Date
  - Category
  - Description (maximum 100 characters)
  - Future entries are disabled


* Deletion and editing of billing entries
  - Amount
  - Date
  - Category


* Manage categories
  - Overview of all categories
  - Creation of new categories (maximum 50 characters)
  - Deletion of categories
  - Color assignment for categories
  - Tags for revenue and expenses


* View
  - Main Window shows last 10, 50 or all entries
  - Search for entries
  - Filter date, revenue, expenses, category
  - Reset Filter -> ("Aufhebbare Filterungen")


* Coloring
  - Entries are colored according to the category


* Statistics (date is changeable)
  - Summary of all entries
  - Summary of revenue and expenses
  - Average revenue and expenses
  - Five highest revenues and expenses


* Datetime filter for statistics
  - Display summary of revenue and expenses for a specific time period
  - Graphical representation of revenue and expenses for a specific time period


## API Documentation
This is the documentation for the Office Lens REST  API.

### Entry creation
Creates a entry in the database for a purchase or revenue.
#### Request
```http
POST /api/v1/entries/create
```
```json
{
    "title": "Lunch Break",
    "category": "Food",
    "date": 1724925218,
    "amount": 5.99,
    "description": "Bought some food"
}
```
#### Response
```json
{
    "status": "success",
    "message": "Entry created successfully."
}
```

### Category creation
Creates a category which must be used when creating a entry.
#### Request
```http
POST /api/v1/categories/create
```
```json
{
    "title": "Lunch Break",
    "color": "#FF0000",
    "tag": "revenue"
}
```
#### Response
```json
{
    "status": "success",
    "message": "Category created successfully."
}
```

### Get entries
Gets all entries and returns them as a JSON object list.
#### Request
```http
GET /api/v1/entries/get
```
#### Response
```json
{
    "status": "success",
    "data": [{'id': 1, 'title': 'External Revenue', 'category': 'General Revenue', 'date': 1724925600, 'amount': 7000.0, 'description': 'External Revenue 123'}, {'id': 2, 'title': 'Desk purchase', 'category': 'General Expense', 'date': 1681293600, 'amount': -800.0, 'description': 'Purchased new Desks'}]

}
```

### Get categories
Gets all categories and returns them as a JSON object list.
#### Request
```http
GET /api/v1/categories/get
```
#### Response
```json
{
    "status": "success",
    "data": [{'id': 1, 'name': 'General Expense', 'color': '#FF8080', 'tag': 'expense'}, {'id': 2, 'name': 'General Revenue', 'color': '#00FF00', 'tag': 'revenue'}]
}
```

### Remove category
Removes a category from the database.
#### Request
```http
GET /api/v1/categories/remove?id=<id>
```
#### Response
```json
{
    "status": "success",
    "message": "Category removed successfully."
}
```

### Remove entry
Removes a entry from the database.
#### Request
```http
GET /api/v1/entries/remove?id=<id>
```
#### Response
```json
{
    "status": "success",
    "message": "Entry removed successfully."
}
```

### Edit entry
Edits a entry in the database.
#### Request
```http
POST /api/v1/entries/edit
```
```json
{
    "id": 1,
    "title": "Lunch Break",
    "category": "Food",
    "date": 1724925218,
    "amount": 5.99,
    "description": "Bought some food"
}
```
#### Response
```json
{
    "status": "success",
    "message": "Entry edited successfully."
}
```