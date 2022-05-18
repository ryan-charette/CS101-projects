#In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package.
#There are several different options for a customer to ship their package:
    #Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
    #Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
    #Drone Shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
#Write a Python program that asks the user for the weight of their package and then tells them:
    #Which method of shipping is cheapest 
    #How much it will cost to ship their package

weight = float(input("How many pounds does your package weight? "))
cost = 0.0
lowest_price = 0.0
cheapest_option = ""

if weight <= 2.0:
  cost = weight * 1.5
elif weight <= 6.0:
  cost = weight * 3.0
elif weight <= 10:
  cost = weight * 4.0
else:
  cost = weight * 4.75

ground = ("Ground Shipping", cost + 20.0)
ground_premium = ("Ground Shipping Premium", 125.0)
drone = ("Drone Shipping", cost * 3)

lowest_price = round(min(ground[1], ground_premium[1], drone[1]), 2)

if lowest_price == ground[1]:
  cheapest_option = ground[0]
elif lowest_price == ground_premium [1]:
  cheapest_option = ground_premium[0]
else:
  cheapest_option = drone[0]

print("Our recommended shipping method is " + cheapest_option + " ($" + '{:.2f}'.format(lowest_price) + ")")
