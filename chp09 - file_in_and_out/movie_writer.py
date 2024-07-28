"""
Real Python Book 1 Chapter 9 - Read and Write CSV Data
"""

import csv
import os

my_path = "C:/Users/Q/Dropbox/Recurrent Commitments/Growth and Learning/Python/RealPython/book1-exercises-master/chp09/practice_files"

my_ratings = [ ['Movie', 'Rating'],
        ['Rebel Without a Cause', '3'],
        ['Monty Python\'s Life of Brian', '5'],
        ['Santa Claus Conquers the Martians', '0'] ]

def csv_write():
    with open(os.path.join(my_path, "movies.csv"), "w") as my_file:
        my_file_writer = csv.writer(my_file)
        my_file_writer.writerows(my_ratings)

def main():
    # Enter main function here
    csv_write()

if __name__ == "__main__":
    main()
