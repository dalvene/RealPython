"""
Pattern matching assignment from Real Python course
"""

import os

my_path = "C:/Users/Q/Dropbox/Recurrent Commitments/Growth and Learning/Python/RealPython/book1-exercises-master/chp09/practice_files/little pics"

def remove_files():
    # Function to remove files
    for current_folder, subfolders, file_names in os.walk(my_path):
        for file_name in file_names:
            print("---")
            current_file = os.path.join(current_folder, file_name)
            print(current_file)
            file_ext = file_name[len(file_name)-4:]
            print(file_ext)
            file_size = os.path.getsize(current_file)
            print(file_size)
            if file_ext == ".jpg" and file_size < 2000:
                os.remove(current_file)
                print("Deleted!")

def main():
    # Enter main function here
    remove_files()

if __name__ == "__main__":
    main()
