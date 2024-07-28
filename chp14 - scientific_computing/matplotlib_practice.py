"""
Real Python Book 1 Chapter 14 - Scientific Computing and Graphing.
Use matplotlib for Plotting Graphs
"""

import os
import numpy as np
from matplotlib import pyplot as plt
# plt.ion()


def dot_plot():
    # Enter a function here
    x_points = np.arange(1, 21)
    baseline = np.arange(0, 20)
    plt.plot(x_points, baseline**2, "g-o", x_points, baseline, "r-^")
    # plt.axis([0, 21, 0, 400])
    plt.title("Amount of Python learned over time")
    plt.xlabel("Days")
    plt.ylabel("Standardized knowledge index score")
    plt.legend(("Real Python", "Other course"), loc=2)
    plt.show()


def bar_chart():
    plt.bar(np.arange(10)*3, np.arange(1,21,2))
    plt.bar(np.arange(10)*3+1, np.arange(1,31,3), color="red")
    plt.xticks(np.arange(10)*3+1, np.arange(1,11), fontsize=20)
    plt.title("Coffee consumption due to sleep deprivation")
    plt.xlabel("Group number")
    plt.ylabel("Cups of coffee consumed")
    plt.legend(("Control group", "Test group"), loc=2)
    plt.show()


def histogram():
    plt.hist(np.random.randn(10000), 20)
    plt.annotate(r"$\hat \mu = 0$", xy=(0, 0), xytext=(0, 300), ha="center",
                 arrowprops=dict(facecolor='black'), fontsize=20)
    path = "../chp14 - scientific_computing"
    # plt.savefig(os.path.join(path, "histogram.png"))
    # plt.savefig(os.path.join(path, "histogram.pdf"))
    plt.show()


def main():
    # Enter main function here
    # dot_plot()
    # bar_chart()
    histogram()


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print(f"Runtime: ---{(time.time() - start_time):.2f}---")