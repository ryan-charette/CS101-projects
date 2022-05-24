#In this project, we will be storing the names and prices of a furniture store’s catalog in variables. 
#You will then process the total price and item list of customers, printing them to the output terminal.

sales_tax = .088
subtotal = 0
itemization = ""

class Furniture:
  def __init__(this, description, price):
    this.description = description
    this.price = price
  def AddItem(this):
    global subtotal
    global itemization
    subtotal += this.price
    itemization += this.description

def Checkout():
  global subtotal
  global sales_tax
  global itemization

  tax = round(subtotal * sales_tax, 2)
  total = subtotal + tax

  print("Items:", end ="")
  print(itemization)
  print("""
Subtotal: $""" + '{:.2f}'.format(subtotal))
  print("Tax 8.8%: $" + '{:.2f}'.format(tax))
  print("Total: $" + '{:.2f}'.format(total))

lovely_loveseat = Furniture("""
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.""", 254.00)
stylish_settee = Furniture("""
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.""", 180.50)
luxurious_lamp = Furniture("""
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.""", 52.15)

lovely_loveseat.AddItem()
luxurious_lamp.AddItem()
Checkout()
