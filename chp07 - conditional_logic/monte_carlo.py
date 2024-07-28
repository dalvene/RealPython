from random import random

candidate_A = 0
candidate_B = 0

for trials in range(0, 10000):
    region1 = random()
    region2 = random()
    region3 =  random()
    if region1 <= 0.87 and (region2 <= 0.65 or region3 <= 0.17):
        candidate_A += 1
    elif region1 > 0.87 and region2 <= 0.65 and region3 <= 0.17:
        candidate_A += 1
    else:
        candidate_B += 1

print(f"Candidate A = {candidate_A} - {candidate_A/100}%, \
Candidate B = {candidate_B} - {candidate_B/100}%")
