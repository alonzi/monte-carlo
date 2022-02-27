import numpy as np
import matplotlib.pyplot as plt

N = 10**1
N = 3*10**3
#N = 10**6
avg = []

def toCoin(x):
    if x==0: return 'heads'
    if x==1: return 'tails'

results = np.random.randint(0,2,N)

print('\n')
print('RNG results =',results)
print('Coin Flips = ',list(map(toCoin,results)))
print('# of heads =',sum(results))
print('# of tails =', N-sum(results))
print('\n')

for result in results:
    if len(avg) == 0: avg.append(result)
    else: avg.append((avg[len(avg)-1]*len(avg)+result) / (len(avg)+1) )

plt.plot(avg)
plt.axhline(y = 0.5, color = 'blue', linestyle = '-')
plt.title("Percentage of Tails to Heads for N flips")
plt.xlabel("Flips")
plt.ylabel("Tails/Heads")
plt.show()