import random


def coin_toss():
    for i in range(5):
        print(f"{'heads' if random.random() <= 0.5 else 'tails'}")

# print(random.uniform(1, 100))
# print(random.randint(1, 100))
# print(random.randrange(0, 101, 5))

# random.seed(1)
# print(random.random())
# print(random.random())

# random.seed(1)
# print(random.random())
# print(random.random())


coin_toss()
