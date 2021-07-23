#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:13:58 2020
@author: dkrajnov
Potsdam

exec(open('/Users/dkrajnov/WORK/python/teaching/stellar_evolution_clock.py').read())


"""

import numpy as np  
import matplotlib.pyplot as plt       

plt.rc('text', usetex=True)
plt.rc('font',family = 'serif', size=15)

#--------------------------------------

t=np.linspace(1e7,1e10,100)                                                                                                                         

m1=0.0434*(np.log10(t))**2 - 1.146*np.log10(t)+7.119    
m2=0.0379*(np.log10(t))**2 - 1.048*np.log10(t)+6.119    


fig,ax =plt.subplots(figsize=(7,6))
im1, = ax.plot(t, 10**m1, label='M$_{TO}$')
im2, = ax.plot(t, 10**m2, label = 'M$_{D}$')
ax.set_yscale('log')
ax.set_xscale('log')

ax.legend(handles=[im1,im2], loc=1)

ax.set_xlabel('Age [yr]')
ax.set_ylabel('Masss [M$_\odot$]')
fig.savefig("3a.pdf")
#plt.show()

print('Mass of the star that leaves MS after 10^7 yr, M=', 10** (0.0434*(np.log10(1e7))**2 - 1.146*np.log10(1e7)+7.119) , ' Msun')
print('Mass of the star that leaves MS after 10^8 yr, M=', 10**(0.0434*(np.log10(1e8))**2 - 1.146*np.log10(1e8)+7.119), ' Msun')
print('Mass of the star that leaves MS after 10^9 yr, M=', 10**(0.0434*(np.log10(1e9))**2 - 1.146*np.log10(1e9)+7.119), ' Msun')
print('Mass of the star that leaves MS after 10^10 yr, M=', 10**(0.0434*(np.log10(1e10))**2 - 1.146*np.log10(1e10)+7.119), ' Msun')
print('')
print('Mass of the dying star after 10^7 yr, M=', 10** (0.0379*(np.log10(1e7))**2 - 1.048*np.log10(1e7)+6.119) , ' Msun')
print('Mass of the dying star after 10^8 yr, M=', 10**(0.0379*(np.log10(1e8))**2 - 1.048*np.log10(1e8)+6.119), ' Msun')
print('Mass of the dying star after 10^9 yr, M=', 10**(0.0379*(np.log10(1e9))**2 - 1.048*np.log10(1e9)+6.119), ' Msun')
print('Mass of the dying star after 10^10 yr, M=', 10**(0.0379*(np.log10(1e10))**2 -1.048*np.log10(1e10)+6.119), ' Msun')
print('')

#from Davor:
#print('Mass of the star that is born 1Myr after BB and burns H, M=', 10**(0.0434*(np.log10(12.7e9))**2 - 1.146*np.log10(12.7e9)+7.119), ' Msun')
print('Mass of the star that is born 1Myr after BB and burns H, M=', 10**(0.0434*(np.log10(13.8e9-1e6))**2 - 1.146*np.log10(13.8e9-1e6)+7.119), ' Msun')
