################################################################################
#                                       pySOM                                  #
#------------------------------------------------------------------------------#
#   Mikel Palmero  &  Miguel Angel Simon Martinez                              #
################################################################################


import numpy as np



# function to define the grid
def grid_def(nx, Lx0, Lx, hb):

    dx = Lx/(nx-1)                              #size of the step in x
    # x = Lx0+dx*np.arange(1,nx)                #definition of the coordinate
    x = np.linspace(Lx0, Lx0+Lx, nx)
    dpx = 2*np.pi*hb/(nx*dx)                    #size of the step in the position

    px = dpx*np.arange(nx/2+1)
    px = np.concatenate((px[:-1],-px[-1:0:-1])) #definition of the momentum

    return x, dx, px, dpx
