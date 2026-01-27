import numpy as np
from goph547lab00.arrays import (
    square_ones,
)


def main():
    # test creating square array of ones
    a_np = np.ones((3,3))
    a = square_ones(3)
    print(f'A_np:\n{a_np}')
    print(f'A:\n{a}')


# 1. Create an array of ones with 3 rows and 5 columns

    a_ones = np.ones((3,5))
    print(f'A_ones:\n{a_ones}')

# 2.Produce an array of NaN with 6 rows and 3 columns

    a_nan = np.empty((6,3))
    a_nan.fill(np.nan)
    print(f'A_nan:\n{a_nan}')

# 3.Create a column vector of odd numbers between 44 and 75

    vector = np.array([[45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73]])
    column_vector = vector.T
    print(f'Column vector of odd numbers between 44 and 75:\n{column_vector}')


# 4.Find the sum of the vector produced in #3

    column_sum = np.sum(column_vector)
    print(f'Sum of column vector:\n{column_sum}')

# 5. Produce the array:
# A=
# [[ 5 7 2],
#  1 -2 3],
#   4 4 4]]

    array_a = np.array([[5, 7, 2], [1, -2, 3], [4, 4, 4]])
    print(f'A = \n{array_a}')

# 6. Using a single command, produce the array:
# B =
# [[ 1 0 0],
#   0 1 0],
#   0 0 1]]

    b = print(f'B = \n{np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])}')


# 7. Perform element-wise multiplication of the arrays A and B from #5 and #6

    array_b = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    element_mult = array_a * array_b
    print(f'Element-wise multiplication of matrices A and B:\n{element_mult}')


# 8. Calculate the dot product (or matrix multiplication) of arrays A and B

    matrix_mult = array_a @ array_b
    print(f'Matrix multiplication of matrices A and B:\n{matrix_mult}')

# 9. Calculate the cross product of arrays A and B

    cross_pdt = np.cross(array_a, array_b)
    print(f'The cross product of matrices A and B:\n{cross_pdt}')

if __name__ == '__main__':
    main()
