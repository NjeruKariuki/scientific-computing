from math import sqrt, pi, exp
from matplotlib import pyplot as plt
import random

'''
3 variables, x,s, and m

if x tends from 0 to 10, by .5, put all x into list
'''
all_x = [x/10 for x in range(0, 100, 5)]

'''randomized variables for more fun'''
s = random.randint(0, len(all_x))
m = random.randint(0, len(all_x))
x = 6

#created function for bell-curve gaussian distribution
def bellGausianFxn(x):
    f = (1/(sqrt(2*pi)*s))*exp(-0.5*((x-m)/s)**2)
    return f

#get y values
results = [bellGausianFxn(x) for x in all_x]

#plotting the results
plt.plot(all_x, results)
plt.show()


