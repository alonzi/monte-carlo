# Introduction to Monte Carlo Simulation
This repository contains a 30 minute session intended for undergraduate students. The topic is 'Introduction to Monte Carlo Simulation'.

## Preface
* The target level is a class of 2nd year UVA students.
* This session fits primarialy in the Systems area pulling heavily from Design and Probability.
* This session sits in the first Systems course.
  * After: the fundamentals of computer programming
  * Purpose: First exercise for students to use the computer as a tool to solve problems
  * Before: complex multi-system pipelines

---

# Warm up question: How many games are played in the NCAA basketball tournament?

# Today's Focus: The Monte Carlo Method

---

# Introduction
![](https://github.com/alonzi/monte-carlo/blob/3449d0f1c22ec12c4106d7fe41a4105da83ef348/images/norbert-sue-munich.jpg)

This is my friend Hussain Zaidi. He is a theoretical physicist and loves puzzles, especially ones that make me look silly.

Let me tell you about the time he got me really good.

## The Monty Hall Problem
![](https://github.com/alonzi/monte-carlo/blob/706070fd4393e3c354cdd5abea0a60ab0aa999f3/images/Monty_open_door.svg.png)

As original seen widely on Let's Make a Deal. 

Here is our definition of the game:
> * There are three doors (labeled 1,2,3)
> * The player will get to open a door at the end and keep what is behind it.
> * Two doors have a goat behind them and the other door has a *Brand New Car* TM.
> * The player will select a door.
> * The host will open a door the player didn't choose revealing a goat.
> * Two doors will remain, one the player chose and the other closed door.
> * The host will let the player switch to the other closed door, if the player wants to.
> * The player will open their door and see what they have won.

The question Hussain put to us and now I put to you is ....

# Should You Switch?
I would like everyone to take two minutes in pairs to discuss and decide on the best course of action.

On the chance you are familar with this problem please defer to your partner.

### (Pete don't forget) Record the results of the deliberations and pause for questions.

## Hussain's Reaction
![](https://github.com/alonzi/monte-carlo/blob/f9434adeb8b6f831f80ab1db36c499bcb094d93d/images/disappointed.jpg)

I was wrong, but refused to believe it. So Hussain gave me the same look this cricket fan gave. But I knew I was right and the way I was going to prove it was with a Monte Carlo simulation. Hussain and his theoretical garbage could not stand up to the awesome power of my simulations ... As it turned out, the simulations proved him correct and I was wrong. But the lesson I learned that day endures. And my goal is to help you learn same lesson.

### When in doubt, just Monte Carlo it.

---
---

# The Monte Carlo Casino
![](https://github.com/alonzi/monte-carlo/blob/f83926a62f869a209d41a5022cb750c8a47930d0/images/Monte_Carlo_Casino,_Monaco_-_interior-_(2)_(32774947955).jpg)

# The Monte Carlo Method

1. Define the set of all possible starting conditions
2. Generate trials by sampling from that set, **APPROPRIATELY**
3. Perform necessary computation for each trial separately
4. Aggregate the results


### N.B. - Every discipline uses different terminology and variations on this approach. Always check to make sure you aren't talking past each other.

# Example 1 - flipping a coin
Let's follow the method for flipping a coin. We want to determine if a coin is 'fair'.

## Exercise
In pairs work out the four steps above for checking the fairness of a coin.

1. Define two possible starting conditions - {Heads,Tails}
2. Generate Trials - flip coins
3. Compute - write down the results
4. Aggregate - calculate estimates

### (Pete don't forget) Record the results of the deliberations and pause for questions.


## The power comes from the so-called "Law of Large Numbers"
![](https://github.com/alonzi/monte-carlo/blob/041a169c4282a1aacce399f3143e0307c39e0b76/images/large-number-of-flips.png)
![](https://github.com/alonzi/monte-carlo/blob/a1dd3651385baff13d4a3df9cecd44f69153de9f/images/Lawoflargenumbersanimation2.gif)

### Corollary, the gambler's fallacy
![](https://github.com/alonzi/monte-carlo/blob/041a169c4282a1aacce399f3143e0307c39e0b76/images/harras.png)

#### Corollary to the corollary, regression to the mean

# Sytems to the rescue
### The ENIAC - c1950
![The ENIAC - c1950](https://github.com/alonzi/monte-carlo/blob/7a370df312a4e01ee24ea8c88796c49621f5e8f4/images/Eniac.jpg)

### Pete's Thesis Experiment - c2010
![Pete's Thesis Experiment - c2010](https://github.com/alonzi/monte-carlo/blob/854ba35ebf88f1c7bb5bdb8f6fc9639b734fbd6b/images/mess.jpeg)


## Exercise - same as last time, but with python functions
1. Define two possible starting conditions - {Heads,Tails}
2. Generate Trials - `np.random.randint(...)`
3. Compute - map RNG results to Heads/Tails - `map(...)`
4. Aggregate - `sum(...)`

### (Pete don't forget) Record the results of the deliberations and pause for questions.

You can see my code here: [examle-1-coin-flip.py](https://github.com/alonzi/monte-carlo/blob/b83b0e47812e5e302b582e57b0ab756e87112ddb/code/example-1-coin-flip.py)

# The Solution to the Monty Hall Problem

## Graph solution
The key is to use the correct basis. Don't think in terms of door numbers (1,2,3). Think in terms of what is behind the door (car,goat).

![](https://github.com/alonzi/monte-carlo/blob/b34e4db381848a0cfb59f443fae57c0a10bd52dd/images/monty-diagram.jpeg)

This diagram shows two choices, car or goat, followed by the strategy of 'stay' or 'switch'. The key is to remember the weight (indicated on the right hand side).


## Monte Carlo Solution
```
import numpy as np

GAMES = 100000
DOORS = [1,2,3]
wins = 0

for i in range(GAMES):
    my_choice = np.random.choice(DOORS)
    car_behind = np.random.choice(DOORS)

    if my_choice != car_behind: wins += 1 # because I win when I switch

print("Win percentage when strategy is 'SWITCH' =", 100.*wins/GAMES)
```
![](https://github.com/alonzi/monte-carlo/blob/96dd2adb7b4962dfa3292164b7c8eaf5b2d9f227/images/Screen%20Shot%202022-03-01%20at%203.10.57%20PM.png)
## Bayes' Solution
![](https://github.com/alonzi/monte-carlo/blob/main/images/Screen%20Shot%202022-03-01%20at%204.27.12%20PM.png)

Full notes on Bayes' [here](https://github.com/alonzi/monte-carlo/blob/main/images/bayes-note.pdf).

### I love Bayes' rule, it's the integration by parts of probability
---

# Recap
lorem ipsum

# Next Time
lorem ipsum

---

# Homework

## Coding Exercises
1. Create a plot showing 10,000 flips and the estimate of the fairness converging ([hint](https://github.com/alonzi/monte-carlo/blob/b83b0e47812e5e302b582e57b0ab756e87112ddb/code/example-1-coin-flip.py))
2. Extend the plot from #1 to include one standard deviation error bars
3. Write a Monte Carlo simulation for 52 doors (i.e. the deck of cards example)
4. Write a Monte Carlo simulation for something you see in your everyday life

## Questions to ponder
1. How many samples/trial/games do I need to run in my simulation?
2. How would you simulate rare processes (e.g. something that only happens 1 in 10,000 times)?
3. What is the relationship between variance and confidence?
4. What is the relationship between probability of an event and your surprise?
5. How would you modify your program if you were to chain multiple steps together for a single game (i.e. What if there were doors behind the doors)?

## If you complete the Homework then Hussain will be like:
![](https://github.com/alonzi/monte-carlo/blob/75498d1484574ba3b86412343f652886f71b2c24/images/happy-fan.jpg)

# Notes
* ![](https://github.com/alonzi/monte-carlo/blob/762c7013f9157e80cd3277a42186b7dcb9fe88a5/Cc-by-nc-sa_icon.svg.png) see https://creativecommons.org/licenses/by-nc-sa/4.0/      
* This session was inspired by:
  * Eric Grimson, John Guttag, and Ana Bell. 6.0002 Introduction to Computational Thinking and Data Science. Fall 2016. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu. License: Creative Commons BY-NC-SA.https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/
  * Hussain Zaidi
* Disappointed Cricket Fan: https://knowyourmeme.com/memes/disappointed-muhammad-sarim-akhtar - https://youtu.be/RL5icIDb_eg
* Doors and a Goat - By Cepheus - Own work, Public Domain, https://commons.wikimedia.org/w/index.php?curid=1234194
* https://en.wikipedia.org/wiki/Let%27s_Make_a_Deal
