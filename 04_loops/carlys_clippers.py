#You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

#You have been provided with three lists:
  #hairstyles: the names of the cuts offered at Carly’s Clippers.
  #prices: the price of each hairstyle in the hairstyles list.
  #last_week: the number of purchases for each hairstyle type in the last week.
#Each index in hairstyles corresponds to an associated index in prices and last_week.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.
total_price = 0
for price in prices:
  total_price += price
average_price = total_price / len(prices)
print("Average Haircut Price: \n$" + str(average_price))

#That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.
new_prices = [price - 5 for price in prices]
print(new_prices)

#Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: \n$" + str(total_revenue))
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: \n$" + str(average_daily_revenue))

#Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
