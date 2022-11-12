import random


def coin_toss():
    for i in range(5):
        print(f"{'Heads' if random.random() <= 0.5 else 'Tails'}")


def random_num_within_range():
    print(random.uniform(1, 10))


def random_int_within_range_inclusive():
    print(random.randint(1, 10))


def random_int_within_stepped_range():
    print(random.randrange(0, 11, 5))


def position_generator():
    random.seed(1)

    print(random.random())
    print(random.random())


coin_toss()

random_num_within_range()

random_int_within_range_inclusive()

random_int_within_stepped_range()

position_generator()
position_generator()
