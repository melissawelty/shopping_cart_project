# shopping_cart.py

from datetime import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
 ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# Info capture / input

total_price = 0 # stores running total of price
selected_ids = []
valid_id = [str(v["id"]) for v in products]


while True:
    select_id = input("Please input product identifier. If no more items input DONE: ") #> "9" (string)  
    select_id = select_id.upper()
    if select_id == "DONE":
        break
    elif select_id in valid_id: 
        selected_ids.append(select_id)
    else:
        print("Invalid Product ID. Please try again.")

#enter wrong number error to keep going and readme file 

# info display / output 



print("---------------------------------")
print("WHOLE PAYCHECK GROCERY")
print("www.wholepaycheckgrocery.com")
print("---------------------------------")
now = datetime.now()
date_time = now.strftime("%D, %r")
print("CHECKOUT AT:", date_time)
print("---------------------------------")

print("SELECTED PRODUCTS:")
for select_id in selected_ids:
    matching_products = [item for item in products if str(item["id"]) == str(select_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    print(matching_product["name"] + " ($" + format(matching_product["price"], ",.2f") + ")" )


print("---------------------------------")
print("SUBTOTAL: $" + format(total_price, ",.2f"))
sales_tax = total_price * .0875
print("TAX: $" + format(sales_tax, ",.2f"))
order_total = sales_tax + total_price
print("TOTAL: $" + format(order_total, ",.2f"))


print("---------------------------------")
print("THANK YOU! COME AGAIN!")
print("---------------------------------")

# ERROR

