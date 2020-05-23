Write a Percolation module in Python to solve the vertical percolation problem we saw in class. 

Your module should make use of the functions we designed in class. Specifically:

  1 Functions to read and write N x N arrays (use numpy) of binary numbers representing a grid of blocked/open sites (from or to text files). 
    Please use the format below for text files.
  2 A function that takes one of the arrays from (1) as input and outputs an array of vacant/ full sites.
  3 A function that takes as input the output from (2) and outputs a boolean indicating whether the system percolates or not.
  4 A function that takes as input a number p between 0-1, an integer N, and generates a random NxN boolean array of blocked/open sites where each site is open with probability p. 
    This function will be useful for testing your code.
  5 I have provided function definitions in the attached percolation.py file. I have provided a main function to test your code in a separate file percolation_tester.py. 
    Your code must work with the main function I have provided.

For section (1) above please use the following text file format: 
  The first row of the text file should contain the integer N. That is the number of rows and columns in the system. 
  The next N rows should contain N 1s and 0s each separated by a space. The 0 indicates a blocked site and the 1 indicates an open site. 
