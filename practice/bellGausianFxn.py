from math import sqrt, pi, exp
from matplotlib import pyplot as plt
import random

'''
3 variables, x,s, and m

if x tends from 0 to 100, by 5, put all x into list of x
'''
all_x = [x/10 for x in range(0, 100, 5)]

''' variables'''
s = random.randint(0, len(all_x))
print(s)
m = random.randint(0, len(all_x))
print(m)
results = []


for x in all_x:
    res = (1/(sqrt(2*pi)*s))*exp(-0.5*((x-m)/s)**2)
    results.append(res)

for res in results:
    print(res)

#plotting the results
plt.plot(all_x, results)
plt.show()


