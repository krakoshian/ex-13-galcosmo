import numpy as np
import matplotlib.pylab as plt

plt.rc('text', usetex=True)
plt.rc('font',family = 'serif', size=15)

_, Age, B1, V1, _, _, B2, V2 = np.loadtxt('tableBell2003.txt').T

def mass_to_light_ratio(a, b, B, V):
    return 10**(a + b * (B - V))
    
def fittingPowerLaw(xdata,ydata):
    from scipy import optimize
    fitfunc = lambda p, x: p[0] + p[1] * x
    errfunc = lambda p, x, y: (y - fitfunc(p, x)) 
    logx = np.log10(xdata)
    logy = np.log10(ydata)
    pinit = [1.0, -1.0]
    if False:
        out = optimize.leastsq(errfunc, pinit,
                       args=(logx, logy),absolute_sigma = True)#, full_output=1)
    elif False:
        out = optimize.curve_fit(lambda x, p1 ,p2: fitfunc([p1,p2],x), logx, logy, absolute_sigma = True)
    else:
        out = optimize.curve_fit(lambda x, p1 ,p2: p1*x**p2, xdata, ydata, absolute_sigma = True)
        print(out)
        out = [x for x in out]
        out[0][0] = np.log10(out[0][0])
    return out[0]    
    
#Colours    
a = [-0.942, -0.628, -0.206]
b = [1.737, 1.305, 0.135]

c = ['tab:blue','tab:orange','tab:green']

fig, ax = plt.subplots(1, 1)

ax.plot(Age, mass_to_light_ratio(a[0], b[0], B1, V1), 'x', c=c[0], label='[Fe/H]=0, B')
ax.plot(Age, mass_to_light_ratio(a[1], b[1], B1, V1), 'x', c=c[1], label='[Fe/H]=0, V')
ax.plot(Age, mass_to_light_ratio(a[2], b[2], B1, V1), 'x', c=c[2], label='[Fe/H]=0, K')

ax.plot(Age, mass_to_light_ratio(a[0], b[0], B2, V2), 'o', c=c[0], label='[Fe/H]=0.3, B')
ax.plot(Age, mass_to_light_ratio(a[1], b[1], B2, V2), 'o', c=c[1], label='[Fe/H]=0.3, V')
ax.plot(Age, mass_to_light_ratio(a[2], b[2], B2, V2), 'o', c=c[2], label='[Fe/H]=0.3, K')

out = fittingPowerLaw(Age, mass_to_light_ratio(a[0], b[0], B1, V1))
ax.plot(Age,10**out[0]*Age**out[1],'-',label='fit: %.2g*Age**%.2g' %(10**out[0],out[1]), c=c[0], ls='-')
out = fittingPowerLaw(Age, mass_to_light_ratio(a[1], b[1], B1, V1))
ax.plot(Age,10**out[0]*Age**out[1],'-',label='fit: %.2g*Age**%.2g' %(10**out[0],out[1]), c=c[1], ls='-')
out = fittingPowerLaw(Age, mass_to_light_ratio(a[2], b[2], B1, V1))
ax.plot(Age,10**out[0]*Age**out[1],'-',label='fit: %.2g*Age**%.2g' %(10**out[0],out[1]), c=c[2], ls='-')

out = fittingPowerLaw(Age, mass_to_light_ratio(a[0], b[0], B2, V2))
ax.plot(Age,10**out[0]*Age**out[1],'-',label='fit: %.2g*Age**%.2g' %(10**out[0],out[1]), c=c[0], ls=':')
out = fittingPowerLaw(Age, mass_to_light_ratio(a[1], b[1], B2, V2))
ax.plot(Age,10**out[0]*Age**out[1],'-',label='fit: %.2g*Age**%.2g' %(10**out[0],out[1]), c=c[1], ls=':')
out = fittingPowerLaw(Age, mass_to_light_ratio(a[2], b[2], B2, V2))
ax.plot(Age,10**out[0]*Age**out[1],'-',label='fit: %.2g*Age**%.2g' %(10**out[0],out[1]), c=c[2], ls=':')

ax.set_xlabel(r'$\mathrm{Age}\ [\mathrm{Gyr}]$')
ax.set_xlim([0,10])
ax.set_ylabel(r'$B-V$')

ax.legend(ncol = 4, bbox_to_anchor=(0.5, -.1), loc='upper center')
fig.set_size_inches(10, 8)
fig.tight_layout()
plt.subplots_adjust(left = 0.1, bottom = 0.3, right = 0.9, top = 0.95)

#plt.show()
fig.savefig("2d.pdf")