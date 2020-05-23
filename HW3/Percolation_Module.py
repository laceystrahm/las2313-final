# *******************************************************
# percolation module
# HW3 Part B
# ENGI E1006

# 1) Functions to read and write N x N arrays (use numpy) of binary numbers 
# representing a grid of blocked/open sites (from or to text files). 

#  Text file format: 
#       The first row of the text file should contain the integer N. 
#       That is the number of rows and columns in the system. 
#       The next N rows should contain N 1s and 0s each separated by a space. 
#       The 0 indicates a blocked site (material trying to flow through ex: clay) 
#       and the 1 indicates an open site (empty).

# 2) A function that takes one of the arrays from (1) as input and outputs an array of vacant/ full sites.

# 3) A function that takes as input the output from (2) and outputs a boolean 
# indicating whether the system percolates or not.

# 4) A function that takes as input a number p between 0-1, an integer N, and 
# generates a random NxN boolean array of blocked/open sites where each site is 
# open with probability p. This function will be useful for testing your code.

# *******************************************************


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def read_grid(input_file):

    """Create a site vacancy matrix from a text file.
    input_file is a file object associated with the
    text file to be read. The method should return
    the corresponding site vacancy matrix represented
    as a numpy array
    """
    
    with open(input_file, 'r') as fp:
        first_line = fp.readline().strip()
        np.loadtxt(fp, first_line)
    return #nxn grid from our file

def write_grid(filename, sites):

    """Write a site vacancy matrix to a file.
    filename is a String that is the name of the
    text file to write to. sites is a numpy array
    representing the site vacany matrix to write
    """
    
    with open(filename, 'w') as fp:
        fp.write(str(len(sites)))
        fp.write('\n')
        np.savetxt(fp, sites, fmt="%d")


def percolate(mat, x, y):

    ''' recursion:
            leave 0's
            change 1's to 2's
            propogate to neighbors
        return 
        
        recursion continues percolation down matrix 
    '''
    
    size = len(mat)
    if x < size and x >= 0 and y < size and y >= 0:
        if mat[x, y] == 0:
            return mat
        
        elif mat[x, y] == 2:
            return mat

        else:
            mat[x, y] = 2
            percolate(mat, x-1, y) #west/left
            percolate(mat, x+1, y) #east/right
            percolate(mat, x, y+1) #south/down
            return mat
    return mat
    
                      
def flow(sites):

    """Returns a matrix of vacant/full sites (1=vacant, 0=blocked)
    sites is a numpy array representing a site vacancy matrix. This
    function should return the corresponding flow matrix generated
    through vertical percolation
    pour water in the top of our matrix (first row)
    Any 1's become 2's to represent water flow
    Any 1's connected to them on the left, right, or bottom also become 2's recursively 
    """

    new_sites = sites.copy()
    for i in range(len(new_sites)):
        percolate(new_sites, i, 0)
    return new_sites


def percolates(flow_matrix):

    """Returns a boolean if the flow_matrix (numpy matrix from make_sites) 
    exhibits percolation (water went from the top to the bottom)
    flow_matrix is a numpy array representing a flow matrix
    """
    
    percolates = False    
    if 2 in any(flow_matrix[-1, :]):
        percolates = True  
    return percolates 


def make_sites(n, p):

    """Returns an nxn site vacancy matrix (2D grid of numbers)
    Generates a numpy array representing an nxn site vacancy
    matrix with site vaccancy probability p (probaility numbers will be a 1/empty)
    """
    
    return (np.random.random((n, n)) < p).astype(int)


def plot(before, after):

    """Plots the before and after matrices using matplotlib
    """
    
    fig, axes = plt.subplots(1, 2)
    axes[0].pcolor(before, cmap='Greys_r')
    axes[0].set_ylim(before.shape[0], 0)
    l = ListedColormap(['black', 'white', 'blue'])
    axes[1].pcolor(after, cmap=l)
    axes[1].set_ylim(before.shape[0], 0)
    plt.show()
