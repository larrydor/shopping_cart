# shopping_cart.py

from datetime import datetime
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# source: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/sendgrid.md
load_dotenv()

taxrate = float(os.getenv("TAX_RATE"))
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "OOPS, please create an environment variable called 'SENDGRID_API_KEY'")
MY_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS", "OOPS, please create an environment variable called 'SENDER_EMAIL_ADDRESS'")
SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
#source= https://github.com/s2t2/shopping-cart-with-email-receipts/blob/master/checkout.py
#sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
#subject = "Sending with SendGrid is Fun"
#content = Content("text/plain", "and easy to do anywhere, even with Python")
#mail = Mail(from_email, to_email, subject, content)
#response = sg.client.mail.send.post(request_body=mail.get())
#print(response.status_code)
#print(response.body)
#print(response.headers)

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


# TODO: write some Python code here to produce the desired output

#taxrate = float(taxrate_env)
now = datetime.today().strftime('%m-%d-%Y %H:%M:%S')
#source: https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python

print("Welcome to The Great Variety Superstore!")

total_purchase = 0

selected_ids = []

while True:
    selected_item = input("Select an item number (1-20) or enter (DONE) when finished shopping: ")
    if selected_item.upper() == "DONE": #source - .upper https://github.com/s2t2/shopping-cart-with-email-receipts/blob/master/checkout.py
        break
    else:
        try:
            matching_products = [item for item in products if str(item["id"]) == str(selected_item)]
            matching_product = matching_products[0]
            selected_ids.append(selected_item)
        except IndexError as e:
            print("Item not found. Please select a valid input.")
        #selected_item = input("Select an item number: ")
        #total_purchase = total_purchase + matching_product["price"]
        #total_purchase = sum([float(item["price"]) for item in selected_ids])
        #source: https://github.com/s2t2/shopping-cart-with-email-receipts/blob/master/checkout.py
        #print(selected_item)
        #matching_products = [item for item in products if str(item["id"]) == str(selected_item)]
        #matching_product = matching_products[0]
        #print(matching_product["name"] + " " + str(matching_product["price"]))
    
    #source: https://github.com/s2t2/shopping-cart-with-email-receipts/blob/master/checkout.py
    #for selected_item in selected_ids:
    #matching_products = [item for item in products if str(item["id"]) == str(selected_item)]
    #matching_product = matching_products[0]
    #total_purchase = total_purchase + matching_product["price"]
    # print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"]))
    # selected_ids.append(matching_product)



print("-----------------------------------")
print("The Great Variety Superstore!")
print("WWW.Great-Variety-SuperStore.COM")
print("Phone:(718)-725-0000")
print("-----------------------------------")
print("CHECKOUT TIME:" + " " + str(datetime.today().strftime('%m-%d-%Y %H:%M')))
#source: https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
print("-----------------------------------")
print("SELECTED PRODUCTS:")

for selected_id in selected_ids:
    #breakpoint() source: Professor Rossetti
    matching_products = [item for item in products if str(item["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    print(matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")
    total_purchase = total_purchase + matching_product["price"]
    #print(selected_ids["name"] + " (" + to_usd(selected_ids["price"]) + ")")
    #matching_products = [item for item in products if str(item["id"]) == str(selected_item)]
    #matching_product = matching_products[0]
    #total_purchase = total_purchase + matching_product["price"]
    #print(matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")
    # I recieved help from Abhishek Swaminathan on getting the code order correct!

tax_total = total_purchase * taxrate
total_total = total_purchase + tax_total

print("-----------------------------------")
print("SUBTOTAL:" + " " + to_usd(total_purchase))
print("TAX:" + " " + to_usd(tax_total))
print("TOTAL:" + " " + to_usd(total_total))
print("-----------------------------------")
print("THANK YOU FOR SHOPPING WITH US!")
print("-----------------------------------")

#print(type(total_purchase))
#print(type(taxrate))

### sendgrid source: https://github.com/s2t2/shopping-cart-with-email-receipts/blob/master/checkout.py
### https://github.com/s2t2/shopping-cart-with-email-receipts/blob/master/sendgrid/receipt_template.html


print("Would you like an emailed receipt?")
user_email_address = input("Please input your email address, or 'N' to opt-out: ")

EMAIL_ADDRESS = user_email_address
#from_email_1 = os.environ.get("MY_EMAIL_ADDRESS" "OOPS, please create an environment variable called 'SENDGRID_API_KEY'")
#to_email_1 = EMAIL_ADDRESS

#if user_email_address.upper() == "Y":
#    print(f"We will send a receipt to {EMAIL_ADDRESS}.")

if user_email_address.upper() in ["N", "NO", "N/A"]:
    print("You've elected to not receive a receipt via email.")
    print("THANK YOU FOR SHOPPING WITH US!")
elif "@" not in user_email_address:
    print("You have entered an invalid email address.")
else:
    print(f"Sending receipt to {EMAIL_ADDRESS}.")

    #formatted_products = []
    #for selected_id in selected_ids:
        #formatted_products[0] = selected_id["name"][0]
        #formatted_product = p
        #if not isinstance(formatted_product["price"], str):
        #formatted_product["price"] = to_usd(p["price"])
        #formatted_products.append(formatted_product)
    
    email_products = []
    for items in range(len(selected_ids)):
        if not selected_ids[items].isnumeric():
            email_product = selected_ids[items]
            email_product["name"] = items["name"]
            email_product["price"] = to_usd(items["price"])
            email_products.append(email_product)
        #source: https://stackoverflow.com/questions/10631473/str-object-does-not-support-item-assignment-in-python

    receipt = {
        "subtotal_price_usd": to_usd(total_purchase),
        "tax_price_usd": to_usd(tax_total),
        "total_price_usd": to_usd(total_total),
        "human_friendly_timestamp": now,
        "products": email_products
    }

    #receipt = {
    #    "subtotal_price_usd": to_usd(total_purchase),
    #    "tax_price_usd": to_usd(tax_total),
    #    "total_price_usd": to_usd(total_total),
    #    "human_friendly_timestamp": now,
    #    "products":
    #}
    
    client = SendGridAPIClient(SENDGRID_API_KEY)
    #subject = "Your Receipt from The Great Variety Superstore"

    #message = Mail(from_email=from_email_1, to_emails=to_email_1)
    message = Mail(from_email=MY_EMAIL_ADDRESS, to_emails=user_email_address)
    message.template_id = SENDGRID_TEMPLATE_ID
    message.dynamic_template_data = receipt
    response = client.send(message)

    if str(response.status_code) == "202":
        print("Email sent successfully!")
    else:
        print("Oh, something went wrong with sending the email.")
        print(response.status_code)
        print(response.body)

    print("Thank You for Shopping at The Great Variety Superstore!")