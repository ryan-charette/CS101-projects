#You’ve recently been hired as a cashier at the local sewing hobby shop, Thread Shed. 
#Some of your daily responsibilities involve tallying the number of sales during the day, calculating the total amount of money made, and keeping track of the names of the customers.
#Unfortunately, the Thread Shed has an extremely outdated register system and stores all of the transaction information in one huge unwieldy string called daily_sales.
#All day, for each transaction, the name of the customer, amount spent, types of thread purchased, and the date of sale is all recorded in this same string. 
#Your task is to use your Python skills to iterate through this string and clean up each transaction and store all the information in easier-to-access lists.

daily_transactions_split = []
transactions_clean = []
customers =[]
sales = []
thread_sold = []
thread_sold_split = []
total_sales = 0

file = open("daily_sales.txt")
daily_sales = ""
for text in file:
  daily_sales += text

#Break up `daily_sales` in easy to understand lists `customers`, `sales`, and `threads_sold`
daily_sales_replaced = daily_sales.replace(";,;", ";")
daily_transactions = daily_sales_replaced.split(",")

for transaction in daily_transactions:
  daily_transactions_split.append(transaction.split(";"))

for transaction in daily_transactions_split:
  items_clean = []
  for item in transaction:
    item_clean = item.strip()
    items_clean.append(item_clean)
  transactions_clean.append(items_clean)

for transaction in transactions_clean:
  customers.append(transaction[0])
  sales.append(transaction[1])
  thread_sold.append(transaction[2])

#Determine the total value of the days sales
for sale in sales:
  total_sales += float(sale.lstrip("$"))
  total_sales = round(total_sales, 2)

#Determine how much thread of any specific color was sold
for sale in thread_sold:
  if "&" not in sale:
    thread_sold_split.append(sale)
  else:
    thread_sold_split += sale.split("&")

def color_count(color):
  count = 0
  for thread in thread_sold_split:
    if thread == color:
      count += 1
  return count

colors = ['red','yellow','green','white','black','blue','purple']
for color in colors:
  print("Thread Shed sold {} threads of {} today.".format(color_count(color), color))
