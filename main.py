import json

# read `expenses.json`
with open("expenses.json", "r") as f:
    text = json.load(f)

# get and print total "price" for all expenses at the "pet store"
cost = 0
pet_store = text["pet store"]
for item in pet_store:
    if item["price"]:
        cost += item["price"]

print(f"total price is {cost} for the pet store")



