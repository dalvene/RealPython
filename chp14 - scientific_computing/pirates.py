"""
Real Python Book 1 Chapter 14 - Scientific Computing and Graphing.
Pirates review exercise
"""

import os
import csv
from matplotlib import pyplot as plt
import numpy as np


def dot_plot(input_data, output_path):
    years = input_data[0]
    temps = input_data[1]
    pirate_nums = input_data[2]
    plt.plot(pirate_nums, temps)
    plt.title("Pirates correlate with temperature")
    plt.xlabel("No. Pirates")
    plt.ylabel("Temperature")
    for n in range(len(years)):
        plt.annotate(str(years[n]), xy=(pirate_nums[n], temps[n]))
    plt.savefig(os.path.join(output_path, "graph_of_pirates.png"))
    plt.show()


def pirates(path):
    # Enter a function here
    file_path = os.path.join(path, "pirates.csv")
    pirate_list = []
    with open(file_path, "r") as my_file:
        my_file_reader = csv.reader(my_file)
        for row in my_file_reader:
            pirate_list.append(row)
        # print(pirate_list)
        headers = pirate_list[0]
        # print(headers)
        del pirate_list[0]
        # print(pirate_list)
        pirate_data = np.array(pirate_list)
        # print(pirate_data)
        pirates_transposed = pirate_data.T
        # print(pirates_transposed)
    return pirates_transposed


def main():
    # Enter main function here
    source_path = ("C:/Users/Q/Dropbox/Recurrent Commitments/Growth and Learning/Python/RealPython/"
                   "book1-exercises-master/chp14/practice_files")
    some_data = pirates(source_path)
    dot_plot(some_data, source_path)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print(f"Runtime: ---{(time.time() - start_time):.2f}---")