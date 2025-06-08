# Author: Vernell Mangum
# Project from Codecademy titled Receipts for Lovely Loveseats
#
# In this project, I will be storing the names and prices of a furniture store’s catalog in variables.
# I will then process the total price and item list of customers, printing them to the output terminal.

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. "

lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black. "

stylish_settee_price = 180.50

luxurious_lamp_description = (
    "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. "
)

luxurious_lamp_price = 52.15

sales_tax = 0.088

# Our First Customer

customer_one_total = 0

customer_one_itemization = ""

# Our customer decided to purchase the Lovely Loveseat

customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

# Our customer has decided to purchase the Luxurious Lamp

customer_one_total += luxurious_lamp_price

customer_one_itemization += luxurious_lamp_description

# Our customer is ready to checkout

# First we have to calculate the sales tax on the total
customer_one_tax = customer_one_total * sales_tax

# Adding that tax to the customer's total
customer_one_total += customer_one_tax

# We should print out the customer's receipt

print("Customer One Items: ")
print(customer_one_itemization)

print("Customer One Total: ")
print(customer_one_total)
