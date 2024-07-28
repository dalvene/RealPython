"""
This is an assignment from RealPython fundamentals, titled 'Cats with hats'. 
"""

# Create a dictionary object of 100 pairs.
# Set keys as sequential integers and all values as zero.
cat_status = {}
for n in range(1,101):
    cat_status[n] = 0

# Loop 100 times. Each time, check every key to see if the loop number is a factor.
# If it is then swap the cat's hat status.
for n in range(1,101):
    for key in cat_status.keys():
        if key % n == 0:
            if cat_status[key] == 0:
                cat_status[key] = 1
            else:
                cat_status[key] = 0

# Print out a list of cats that have a hat at the end.
for n in range(1, 101):
    if cat_status[n] == 1:
        print(f"Cat {n} has a hat")
