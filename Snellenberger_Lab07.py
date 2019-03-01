# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

def calc_frequencies_and_modes(matrix,k_over_m):
    val, vect = np.linalg.eigh(matrix)
    freq = np.sqrt(val)
    return freq, vect


M = np.array([[2,-1],
              [-1,2]
              ])
freq, vect = calc_frequencies_and_modes(M,1) #gives 1 and square root 3 as frequencies and gives expected eigenvectors

def calc_compontents_from_initial_conditions(x_init,modes):
    a = x_init @ modes[:,0]
    b = x_init @ modes[:,1]
    return a,b

x = 1/np.sqrt(2)*np.array([1,-1])
a,b = calc_compontents_from_initial_conditions(x,vect)
print(a,b)
#v1 is 1,1, which gives a at 1 and b at 0
#v2 is 1,-1 which gives a at 0 and b at 1
#[0,1] gives .5 for both a and b
#all of these are what we expect

t_init = 0
t_end = 10
N_times = 1000

time = np.linspace(t_init, t_end, num=N_times)
time = time.reshape(N_times, 1)

def calc_pos_of_masses(a, b, freq, time, modes):
    x_pos = (a*np.cos(freq[0]*time)*modes[:,0] 
        + b*np.cos(freq[1]*time)*modes[:,1])
    return x_pos

x_pos = calc_pos_of_masses()

def plot_motion_of_masses(x, time, title='bad title'):
    """
    Function to make a plot of motion of masses as a function of time. The time
    should be on the vertical axis and the position on the horizontal axis.
    Parameters
    ----------
    x : array of position, N_times by 2 elements
        The array of positions, set up so that x[:, 0] is the position of mass
        1 relative to equilibrium and x[:, 1] is the position of mass 2.
    time : array of times
        Times at which the positions have been calculated.
    title : str
        A descriptive title for the plot to make grading easier.
    """
    # Nothing special about these, but they look nice
    x1_equilibrium_pos = 3
    x2_equilibrium_pos = 6

    x1 = x[:, 0] + x1_equilibrium_pos
    x2 = x[:, 1] + x2_equilibrium_pos

    plt.plot(x1, time, label='Mass 1')
    plt.plot(x2, time, label='Mass 2')
    plt.xlim(0, 9)
    plt.legend()
    plt.title(title)
    
plot_motion_of_masses(x_pos, time, title='bad title')

#this is not finished