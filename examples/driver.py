import numpy as np
from goph547lab00.arrays import (
square_ones,
)
def main():
    #test creating square array of ones
    A_np = np.ones((3,3))
    A = square_ones(3)
    print(f'A_np:\n{A_np}')
    print(f'A:\n{A}')


if __name__ == '__main__':
    main()

#1. Create an array of ones with 3 rows and 5 columns


#2.Produce an array of NaN with 6 rows and 3 columns


#3.Create a column vector of odd numbers between 44 and 75


#4.Find the sum of the vector produced in #3


#5. Produce the array:
"""A=
[[ 5 7 2],
   1 -2 3],
   4 4 4]]"""


#6. Using a single command, produce the array:
"""B = 
[[ 1 0 0],
   0 1 0],
   0 0 1]]"""


#7. Perform element-wise multiplication of the arrays A and B from #5 and #6


#8. Calculate the dot product (or matrix multiplication) of arrays A and B


#9. Calculate the cross product of arrays A and B