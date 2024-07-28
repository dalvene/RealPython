"""
Real Python Book 1 Chapter 9 - Read and Write CSV Data
"""

import csv
import os

my_path = "C:/Users/Q/Dropbox/Recurrent Commitments/Growth and Learning/Python/RealPython/book1-exercises-master/chp09/practice_files"

def wonka():
    with open(os.path.join(my_path, "wonka.csv"), "r") as my_file:
        my_file_reader = csv.reader(my_file)
        next(my_file_reader)
        for first_name, last_name, reward in my_file_reader:
            print("{} {} got: {}".format(first_name, last_name, reward))

def main():
    # Enter main function here
    wonka()

if __name__ == "__main__":
    main()
