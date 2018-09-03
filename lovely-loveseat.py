# Catalog
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x " \
                              "30 inches deep. Red or white."
lovely_loveseat_price = 254.00
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches " \
                             "deep. Black."
stylish_settee_price = 180.50
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

# Sales Tax
sales_tax = 0.088

# Customer 1 - initialisation
customer_one_total = 0
customer_one_itemization = ""

# Customer 1 - purchases
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description + "\n"
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# Customer 1 - checkout
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# Customer 1 - create receipt
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print("%.2f" % customer_one_total)
print("\n")

# Customer 2 - initialisation
customer_two_total = 0
customer_two_itemization = ""

# Customer 2 - purchases
customer_two_total += stylish_settee_price
customer_two_itemization += stylish_settee_description + "\n"
customer_two_total += luxurious_lamp_price
customer_two_itemization += luxurious_lamp_description

# Customer 2 - checkout
customer_two_tax = customer_two_total * sales_tax
customer_two_total += customer_two_tax

# Customer 2 - create receipt
print("Customer Two Items:")
print(customer_two_itemization)
print("Customer Two Total:")
print("%.2f" % customer_two_total)
