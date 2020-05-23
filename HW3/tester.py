# *******************************************************
# HW 3
# ENGI E1006

# Doing another type of simulation
# physical surface we are going to flow water through

# probability here has to do with the density of the material or something 
# like that, that we measured phsyical on the actual stuff 

# *******************************************************


import percolation as perc


def main():
    A = perc.make_sites(25, 0.65)
    perc.write_grid('test.txt', A)
    infile = open('test.txt', 'r')
    B = perc.read_grid(infile)
    C = perc.flow(B)
    if perc.percolates(C):
        print('percolates')
    else:
        print('does not percolate')

    perc.plot(B, C)

if __name__ == "__main__":
    main()
