from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
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


# 10.Load the image rock_canyon.jpg

    image = np.asarray(Image.open('C:/Users/zcmit/Desktop/python/GOPH547/GOPH547-w2026-lab00-stZM/examples/rock_canyon.jpg'))
    print(repr(image))


# 11. Plot the image using the imshow() function. What is the shape of the array(s)
# corresponding to this image?

    imageplot = plt.imshow(image)

    plt.title('Initial Image plot')
    plt.axis('off')
    plt.show()

    # The shape of the arrays corresponding to this array are (296, 474, 3)

# 12.Re-open the image converting to grayscale

    gray_image = np.asarray(
        Image.open('C:/Users/zcmit/Desktop/python/GOPH547/GOPH547-w2026-lab00-stZM/examples/rock_canyon.jpg')
        .convert('L')
    )
    print(repr(gray_image))

    plt.imshow(gray_image, cmap='gray')
    plt.axis('off')
    plt.title('Grayscale Image')
    plt.show()

# 13. Using only Python/Numpy commands (not the GUI tool), produce a new
# smaller image array (called small_gray_image) that includes only the
# pinnacle/pillar near the middle left of the image.

    small_gray_image = gray_image[165:230, 105:145]

    plt.imshow(small_gray_image, cmap='gray')
    plt.title("Greyscale pillar")
    plt.axis('off')
    plt.show()

# 14. For the original image rock_canyon.jpg, make subplot with two plots:
# i) with the x-coordinate on the horizontal axis and colour values on the vertical axis and
# ii) with the y-coordinate on the vertical axis and colour values on the horizontal axis.
# In each plot, include four lines/series showing the mean R, G, B, and mean of
# the RGB channels (i.e. in the first graph, mean along the y-direction plotted
# along the x-coordinate and in the second graph, mean along the x-direction
# plotted against the y-coordinate). Colour the R, G, and B curves red, green, and
# blue and the mean RGB as a thicker black line.

    image = np.asarray(
        Image.open('C:/Users/zcmit/Desktop/python/GOPH547/GOPH547-w2026-lab00-stZM/examples/rock_canyon.jpg'))

    R = image[:, :, 0]
    G = image[:, :, 1]
    B = image[:, :, 2]

    mean_R_x = np.mean(R, axis=0)
    mean_G_x = np.mean(G, axis=0)
    mean_B_x = np.mean(B, axis=0)
    mean_RGB_x = np.mean(image, axis=(0, 1))  # WRONG for plot
    # Correct mean RGB per x:
    mean_RGB_x = np.mean(image, axis=0).mean(axis=1)

    mean_R_y = np.mean(R, axis=1)
    mean_G_y = np.mean(G, axis=1)
    mean_B_y = np.mean(B, axis=1)
    mean_RGB_y = np.mean(image, axis=1).mean(axis=1)

    x = np.arange(image.shape[1])  # width
    y = np.arange(image.shape[0])  # height

    plt.figure(figsize=(12, 5))

    # -------- Plot 1: mean vs X --------
    plt.subplot(1, 2, 1)
    plt.plot(x, mean_R_x, 'r', label='Mean R')
    plt.plot(x, mean_G_x, 'g', label='Mean G')
    plt.plot(x, mean_B_x, 'b', label='Mean B')
    plt.plot(x, mean_RGB_x, 'k', linewidth=2, label='Mean RGB')

    plt.xlabel('X Coordinate (pixels)')
    plt.ylabel('Color Value')
    plt.title('Mean RGB Values vs X Coordinate')
    plt.legend()

    # -------- Plot 2: mean vs Y --------
    plt.subplot(1, 2, 2)
    plt.plot(mean_R_y, y, 'r', label='Mean R')
    plt.plot(mean_G_y, y, 'g', label='Mean G')
    plt.plot(mean_B_y, y, 'b', label='Mean B')
    plt.plot(mean_RGB_y, y, 'k', linewidth=2, label='Mean RGB')

    plt.xlabel('Color Value')
    plt.ylabel('Y Coordinate (pixels)')
    plt.title('Mean RGB Values vs Y Coordinate')
    plt.legend()

    plt.tight_layout()
    plt.show()


# 15. Make sure to include axis labels, a title, and a legend on each subplot
# summarizing the RGB channels of the image.


# 16. After you are satisfied with your subplots, save the subplot figure as a file
# called rock_canyon_RGB_summary.png file in your examples/ directory
# using the savefig() function from matplotlib.

    plt.savefig('C:/Users/zcmit/Desktop/python/GOPH547/GOPH547-w2026-lab00-stZM/examples/rock_canyon_RBG_summary.png')

if __name__ == '__main__':
    main()
