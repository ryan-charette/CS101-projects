#You are a physics teacher preparing for the upcoming semester. 
#You want to provide your students with some functions that will help them calculate some fundamental physical properties.

#Write a function that takes an input temperature in Fahrenheit and converts it to that temperature in Celsius
#Write a function that takes an input temperature in Celsius and converts it to that temperature in Fahrenheit 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) / 1.8
  return c_temp
def c_to_f(c_temp):
  f_temp = (c_temp * 1.8) + 32
  return f_temp

#Define a function that takes in mass and acceleration and returns force.
#Define a function that takes in mass, acceleration, and distance and returns work.
#The work function should call the get_force function
def get_force(mass, acceleration):
  return mass * acceleration
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

#Define a function that takes in mass and c and returns energy.
#Set c to have a default value of the speed of light
def get_energy(mass, c = 3*10**8):
  return mass * c**2


