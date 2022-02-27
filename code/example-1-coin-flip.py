import numpy as np

N = 10

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
