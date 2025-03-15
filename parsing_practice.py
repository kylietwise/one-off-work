### script to practice parsing ###

'''JSON'''

test = {
  "users": [
    {
      "id": 1,
      "name": "Alice Johnson",
      "email": "alice@example.com",
      "orders": [
        {
          "order_id": 101,
          "date": "2024-03-10",
          "total": 150.75,
          "items": [
            {"product_id": 1, "name": "Laptop", "price": 1200.99, "quantity": 1},
            {"product_id": 2, "name": "Mouse", "price": 25.50, "quantity": 2}
          ]
        },
        {
          "order_id": 102,
          "date": "2024-03-12",
          "total": 75.00,
          "items": [
            {"product_id": 3, "name": "Keyboard", "price": 75.00, "quantity": 1}
          ]
        }
      ]
    },
    {
      "id": 2,
      "name": "Bob Smith",
      "email": "bob@example.com",
      "orders": [
        {
          "order_id": 103,
          "date": "2024-03-11",
          "total": 200.50,
          "items": [
            {"product_id": 4, "name": "Monitor", "price": 200.50, "quantity": 1}
          ]
        }
      ]
    },
    {
      "id": 3,
      "name": "Charlie Davis",
      "email": "charlie@example.com",
      "orders": []
    }
  ],
  "products": [
    {"product_id": 1, "name": "Laptop", "category": "Electronics", "stock": 5},
    {"product_id": 2, "name": "Mouse", "category": "Accessories", "stock": 20},
    {"product_id": 3, "name": "Keyboard", "category": "Accessories", "stock": 10},
    {"product_id": 4, "name": "Monitor", "category": "Electronics", "stock": 7}
  ]
}

import json
import pandas as pd 
import numpy as np

product_ids = []
names = []

for x in (test["products"]):
    product_ids.append(x["product_id"])
    names.append(x["name"])

df = pd.DataFrame({"product_ids":product_ids, "names": names})
# print(df)

## extract all orders for user 1 ####

# test - 
    # users
        # id, where id = 1
            #orders
                # list of orders, 
                    # items 
                        # list of dictionaries with name in it 

products = []
for user in test["users"]:
    if user["id"] == 1:
        for order in user["orders"]:
            for item in order["items"]:
                products.append(item["name"])


# print(products) # prints all product names for user 1

## get all the names of the users
# test
    # users
        # name

names = []

for user in test["users"]:
    names.append(user["name"])

# print(names)


## find the email address of user 2

for user in test["users"]:
    if user["id"] == 2:
        print(user["email"])


## how many users have made orders
        
# test
    # users
        # where count(order_id) > 0
import math

user_count = 0
for user in test["users"]:
    if user["orders"]:
        user_count += 1

print(user_count)


    