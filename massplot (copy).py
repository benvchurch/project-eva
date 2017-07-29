from __future__ import division

import numpy as np
from scipy import special
from numpy import log, exp, sin ,cos, pi, log10, sqrt
from scipy.integrate import quad, dblquad, cumtrapz
from matplotlib import pyplot as plt
import time

import CDM_SubHalo_Potential

#integral precision
p = 2

#num plot points
num = 50

params = { 
   'axes.labelsize': 24, 
   'axes.titlesize': 22,  
   'legend.fontsize': 20, 
   'xtick.labelsize': 24, 
   'ytick.labelsize': 24, 
   'text.usetex': True,
   'figure.figsize': [10,8], # instead of 4.5, 4.5
   'lines.linewidth': 2,
   'xtick.major.pad': 15, 
   'ytick.major.pad': 15, 
   'figure.subplot.bottom': 0.12,
   'figure.subplot.top': 0.95,
   'figure.subplot.left': 0.2,
   #'font.size': 22
   }   
plt.rcParams.update(params)


D = np.logspace(0, 5, num)
T_age = 10**4


def main():
	
	plt.loglog(D, map(lambda x : CDM_SubHalo_Potential.VelocityDispersionMassDownTo(x, 0.1, int(10**p)), D))
	plt.xlabel(r'$r(pc)$')
	plt.ylabel(r'$ \Delta v \: (km/s)$')
	plt.show()

if __name__ == "__main__":
    main()

    

