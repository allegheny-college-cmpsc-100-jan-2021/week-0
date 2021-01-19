#!/usr/bin/env python3

shopping_list = [
    "screwdriver", 
    "wire", 
    "wall plug",
    "spark plug", 
    "candy bar"
]

store_inventory = {
    "screwdriver": {
        "quantity": 20, 
        "price": 2.25
    },
    "wire": {
        "quantity": 12, 
        "price": .79
    },
    "wall plug": {
        "quantity": 10, 
        "price": 1.00
    },
    "spark plug": {
        "quantity": 49, 
        "price": .50
    },
    "candy bar": {
        "quantity": 12, 
        "price": .99
    }
}

tax = .08
total = 0

# TODO: Iterate over each item in the shopping list and
#       1. Add the price of the item to total
#       2. Subtract 1 from the store inventory
    
print("Subtotal:",total)
print("Total:",total + total * tax)

# TODO: Iterate over the inventory and print the new 
#       quantities remaining (should come out to
#       original -- see above -- minus 1).