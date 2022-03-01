import numpy as np

GAMES = 100000
DOORS = [1,2,3]
wins = 0

for i in range(GAMES):
    my_choice = np.random.choice(DOORS)
    car_behind = np.random.choice(DOORS)

    if my_choice != car_behind: wins += 1 # because I win when I switch

print("Win percentage when strategy is 'SWITCH' =", 100.*wins/GAMES)
