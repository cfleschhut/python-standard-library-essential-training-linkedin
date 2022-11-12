import random
import string

moves = ["rock", "paper", "scissors"]

print(random.choice(moves))

roulette_wheel = ["black", "red", "green"]
weights = [18, 18, 2]

print(random.choices(roulette_wheel, weights, k=10))

sample_letters = random.sample(string.ascii_uppercase, 6)
print(sample_letters)

players = ["Bill", "Jane", "Joe", "Sally", "Mike", "Lindsay"]
random.shuffle(players)

print(players)

result = random.sample(string.ascii_uppercase, k=len(string.ascii_uppercase))
# random.shuffle(result)
print("".join(result))
