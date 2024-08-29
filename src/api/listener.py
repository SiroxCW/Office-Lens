
from flask import Flask, request
from src.api import entries, categories
from json import loads

with open("config.json", "r") as file:
    config = loads(file.read())
influxdb_host = config["influxdb"]["host"]
influxdb_bucket = config["influxdb"]["bucket"]
influxdb_organization = config["influxdb"]["organization"]
influxdb_token = config["influxdb"]["token"]

app = Flask(__name__)

@app.route("/api/v1/entries/edit", methods=["POST"])
def edit_entry():
    data = request.form
    id = data.get("id")
    title = data.get("title")
    category = data.get("category")
    date = data.get("date")
    amount = data.get("amount")
    description = data.get("description")
    response = entries.edit(id, title, category, date, amount, description)
    if response:
        return {"status": "success", "message": "Entry edited successfully."}
    else:
        return {"status": "failed", "message": response}

@app.route("/api/v1/categories/remove", methods=["GET"])
def remove_category():
    id = request.args.get("id")
    response = categories.remove(id)
    if response:
        return {"status": "success", "message": "Category removed successfully."}
    else:
        return {"status": "failed", "message": response}

@app.route("/api/v1/entries/remove", methods=["GET"])
def remove_entry():
    id = request.args.get("id")
    response = entries.remove(id)
    if response:
        return {"status": "success", "message": "Entry removed successfully."}
    else:
        return {"status": "failed", "message": response}

@app.route("/api/v1/entries/get", methods=["GET"])
def get_entries():
    response = entries.get()
    return {"status": "success", "data": response}

@app.route("/api/v1/categories/get", methods=["GET"])
def get_categories():
    response = categories.get()
    return {"status": "success", "data": response}

@app.route("/api/v1/categories/create", methods=["POST"])
def create_category():
    data = request.form
    title = data.get("title")
    color = data.get("color")
    tag = data.get("tag")
    response = categories.create(title, color, tag)
    if response:
        return {"status": "success", "message": "Category created successfully."}
    else:
        return {"status": "failed", "message": response}


@app.route("/api/v1/entries/create", methods=["POST"])
def create_entry():
    data = request.form
    title = data.get("title")
    category = data.get("category")
    date = data.get("date")
    amount = data.get("amount")
    description = data.get("description")
    response = entries.create(title, category, date, amount, description)
    if response:
        return {"status": "success", "message": "Entry created successfully."}
    else:
        return {"status": "failed", "message": response}

@app.route("/")
def description():
    return "This is the API listener for Office Lens. Please see the documentation for more information."

def start():
    app.run()
