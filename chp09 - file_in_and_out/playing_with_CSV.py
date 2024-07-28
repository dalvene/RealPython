"""
Real Python Book 1 Chapter 9 - Read and Write CSV Data review exercises
"""

import os
import csv

def read_CSV(my_path):
    # Function to read a CSV and print the rows.
    with open(os.path.join(my_path, "pastimes.csv"), "r") as my_r_file:
        my_file_read = csv.reader(my_r_file)
        content = []
        next(my_file_read)
        for row in my_file_read:
            print("{} is good at {}".format(row[0], row[1]))
            if row[1].lower().find("fighting") >= 0:
                print("Can fight")
                row.append("Combat")
                content.append(row)
            else:
                print("Can't fight")
                row.append("Other")
                content.append(row)
    print(content)
    return content
            
def write_CSV(my_path, content_list):
    # Function to write a CSV and print the rows.
    write_list = ["Name", "Favourite Pastime", "Type of Pastime"]
    with open(os.path.join(my_path, "categorized pastimes.csv"), "w") as my_w_file:
        my_file_write = csv.writer(my_w_file)
        my_file_write.writerow(write_list)
        my_file_write.writerows(content_list)
    

def main():
    # Enter main function here
    my_path = "C:/Users/Q/Dropbox/Recurrent Commitments/Growth and Learning/Python/RealPython/book1-exercises-master/chp09/practice_files"
    content_list = read_CSV(my_path)
    write_CSV(my_path, content_list)

if __name__ == "__main__":
    main()
