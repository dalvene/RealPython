import os
import glob

my_path = "C:/Users/Q/Dropbox/Recurrent Commitments/Growth and Learning/Python/RealPython/book1-exercises-master/chp09/practice_files/images"

# Get a list of all files and folders
## all_file_paths = os.listdir(my_path)

## Question 1: Display the list in series 
#for path in all_file_paths:
#    print(path)

# Question 2: Find possible PNG files
##possible_files = os.path.join(my_path, "*.png")
##
##for file_name in glob.glob(possible_files):
##    print(file_name)

# Question 3: Rename PNG files
# print(os.walk(my_path))
for current_folder, subfolders, file_names in os.walk(my_path):
    for file_name in file_names:
        # print(os.path.join(current_folder, file_name))
        if file_name[len(file_name)-4:] == ".jpg":
            print(file_name)
            full_name = os.path.join(current_folder, file_name)
            new_name = full_name[0:len(full_name)-4] + ".png"
            os.rename(full_name, new_name)
            print(new_name)
            if os.path.exists(new_name):
                print(f"File {full_name} renamed to {new_name}")
