"""
Real Python Book 1 Chapter 9 - Assignment: Create a high scores list from CSV data
"""

import os
import csv

def read_CSV(my_path):
    # Function to read a CSV
    with open(os.path.join(my_path, "scores.csv"), "r") as my_file:
        my_file_read = csv.reader(my_file)
        #Make a dictionary
        high_scores = {}
        for row in my_file_read:
            if row[0] not in high_scores.keys() or high_scores[row[0]] < row[1]:
                high_scores[row[0]] = row[1]
        # Can this be done with a dict comprehension?
        # high_scores = {row[0]:row[1] for row in my_file_read if row[0] not in high_scores.keys() or high_scores[row[0]] < row[1]}
        return high_scores

def main(my_path):
    # Enter main function here
    high_scores = read_CSV(my_path)
    for n in sorted(high_scores.items()):
        print(n[0], n[1])
    #print(sorted(high_scores.items()))

if __name__ == "__main__":
    my_path = "C:/Users/Q/Dropbox/Recurrent Commitments/Growth and Learning/Python/RealPython/book1-exercises-master/chp09/practice_files"
    main(my_path)
