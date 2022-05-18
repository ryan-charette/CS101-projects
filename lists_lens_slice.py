#You work at Len’s Slice, a new pizza joint in the neighborhood. 
#You are going to use your knowledge of Python lists to organize some of your sales data.

todays_revenue = 0
pizzas_with_prices = []
quantity_price_pizza = []
best_sellers = []

pizzas = ["cheese", "pepperoni", "meat lovers", "supreme", "hawaiian", "margherita", "veggie"]
prices = [2.0, 2.5, 3.0, 3.0, 3.5, 2.5, 3.0]

num_cheap_slices = prices.count(2.0) + prices.count(2.5)
num_pizzas = len(pizzas)

for i in range(len(pizzas)):
  pizzas_with_prices.append([prices[i], pizzas[i]])

for i in range(len(pizzas)):
    quantity_price_pizza.append([8] + pizzas_with_prices[i])

def buy_pizza():
    global todays_revenue
    input_checker = 0
    pizza_sold = input("Enter purchased pizza: ")
    for i in range(len(quantity_price_pizza)):
        if pizza_sold == quantity_price_pizza[i][-1]:
            quantity_price_pizza[i][0] -= 1
            todays_revenue += quantity_price_pizza[i][1]
            input_checker += 1
            if quantity_price_pizza[i][0] == 0:
                print("Sold out of " + str(quantity_price_pizza[i][-1]))
                sold_out = quantity_price_pizza[i].pop(-1)
                best_sellers.append(sold_out)
        elif input_checker == 0 and i == len(quantity_price_pizza) - 1:
            print("Invalid input")
    
def main():
    global best_sellers

    print("We sell " + str(num_pizzas) + " different kinds of pizza! Now selling " + str(num_cheap_slices) + " kinds for under $3!")
    print(pizzas_with_prices)

    while True:
        buy_or_end = input("Press [1] to enter a purchase or [2] to close register and end day: ")
        if buy_or_end == "1":
            buy_pizza()
        elif buy_or_end == "2":
            break
        else:
            print("Invalid Input.")

    popularity_list = sorted(quantity_price_pizza)
    for i in range(len(popularity_list)):
        popularity_list[i].pop(0)
        popularity_list[i].pop(0)
    if len(best_sellers) != 0:
        popularity_list.insert(0, best_sellers)
        
    print("Our top 3 best selling pizzas today were " + str(popularity_list[:3]))
    print("Today's revenue was: $" + str(todays_revenue))

main()
