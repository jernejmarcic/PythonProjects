from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.College
collection = db.placeholdertext

vnos = {
        "name": input("Name of College: "),
        "loc": [input("City: "), input("Country: ")],
        "program": [input("Enter desired masters: "), input("Enter desired undegrad: ")],
        "pointsIB": [int(input("Enter IB points avg: ")), int(input("Enter IB points min: "))],
        "price": {"value": int(input("Enter price in €: ")), "unit":"EUR" }
        }

collection.insert_one(vnos)
find = collection.find()

for f in find:
    print(f)
