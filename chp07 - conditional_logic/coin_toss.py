from random import randint

heads = 0
tails = 0

for trials in range(0, 10000):
    while randint(0,1) == 0:
        tails += 1
    heads += 1

print(f"heads = {heads}, tails = {tails}, ratio = {heads/tails}")
