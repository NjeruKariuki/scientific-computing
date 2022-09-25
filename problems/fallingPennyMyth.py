'''
simple model: 1

FALLING PENNY MYTH

You might have heard that a
penny dropped from the top of the Empire State Building would be going so
fast when it hit the pavement that it would be embedded in the concrete; or
if it hit a person, it would break their skull. Let's prove if this is true: 

formulas:

h = at^2/2
t = sqrt(2h/a)

given: a = 9.8m/s^2
empire state building height: h = 381m 
t = 8.8s 

'''
import math

#vars and parameters
a = 9.8
h = 381 

#time to hit ground
t = math.sqrt(2*h/a)

#velocity after t seconds
v = a * t

#print outputs
print(f"time to hit ground: {t} seconds.")
print(f"Coin velocity when it hits the ground is : {v} m/s^2.")