import numpy as np
import matplotlib.pylab as plt

plt.rc('text', usetex=True)
plt.rc('font',family = 'serif', size=15)

_, Age, B1, V1, _, _, B2, V2 = np.loadtxt('tableBell2003.txt').T

fig, ax = plt.subplots(1, 1)

ax.plot(Age,B1-V1,label='[Fe/H]=0')
ax.plot(Age,B2-V2,label='[Fe/H]=0.3')

ax.set_xlabel(r'$\mathrm{Age}\ [\mathrm{Gyr}]$')
ax.set_xlim([1,10])
ax.set_ylabel(r'$B-V$')

ax.legend()
fig.tight_layout()

#plt.show()
fig.savefig("2b.pdf")