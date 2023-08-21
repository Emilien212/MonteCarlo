import random
import math

total = 0
m = 10

for _ in range(m):
    n = 1000000
    In = 0

    for _ in range(n):
        bag = ["R"]*5 + ["B"]*2 + ["V"]*1
        first = random.choice(bag)
        bag.remove(first)
        second = random.choice(bag)
        if first == second:
            In += 1

    print(In/n)
    print(f"Answer : 22/56 ({22/56})")

print(f"Average 10 runs {round(total/m, 5)}")