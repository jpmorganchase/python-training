# coding: utf-8

import numpy as np


def mandelbrot(X, Y, max_iterations=1000, verbose=True):
    """Computes the Mandelbrot set.

    Returns a matrix with the escape iteration number of the mandelbrot
    sequence. The matrix contains a cell for every (x, y) couple of the
    X and Y vectors elements given in input. Maximum max_iterations are
    performed for each point
    :param X: set of x coordinates
    :param Y: set of y coordinates
    :param max_iterations: maximum number of iterations to perform before
        forcing to stop the sequence
    :param show_out: flag indicating whether to print on console which line
        number is being computed
    :return: Matrix containing the escape iteration number for every point
        specified in input
    """

    # init the output array
    out_arr = np.zeros((len(Y), len(X)))

    # Iterate of the y coordinates
    for i, y in enumerate(Y):
        for j, x in enumerate(X):
            n = 0
            c = x + 1j*y
            z = c
            while (n < max_iterations) and (abs(z) <= 2):
                z = z*z + c
                n += 1
            out_arr[i, j] = n

    return out_arr
