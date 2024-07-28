"""
Real Python Book 1 Chapter 14 - Scientific Computing and Graphing.
Use Numpy for Matrix Manipulation
"""

import numpy as np


def exercise1():
    # Enter a function here
    first_matrix = np.arange(3, 12)
    first_matrix = first_matrix.reshape(3, 3)
    print("matrix: ", first_matrix)
    return first_matrix


def exercise2(matrix):
    print("Minimum: ", np.min(matrix))
    print("Maximum: ", np.max(matrix))
    print("Mean: ", np.mean(matrix))


def exercise3(matrix):
    square_matrix = matrix ** 2
    print("square matrix: ", square_matrix)
    return square_matrix


def exercise4(matrix1, matrix2):
    third_matrix = np.vstack([matrix1, matrix2])
    print("vstack: ", third_matrix)
    return third_matrix


def exercise5(matrix1, matrix2):
    dot_matrix = np.dot(matrix1, matrix2)
    print("dot matrix: ", dot_matrix)


def exercise6(matrix):
    print("reshape: ", matrix.reshape(3, 3, 2))


def main():
    # Enter main function here
    first_matrix = exercise1()
    exercise2(first_matrix)
    second_matrix = exercise3(first_matrix)
    third_matrix = exercise4(first_matrix, second_matrix)
    exercise5(third_matrix, first_matrix)
    exercise6(third_matrix)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print(f"Runtime: ---{(time.time() - start_time):.2f}---")