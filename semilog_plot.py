import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


t = np.arange(0.01,20.0, 0.01)

z = np.arange(100,13000,100) # depth

dtm= 70
dtml = 200
c = 0.000245

dtn= dtm + (dtml - dtm)*np.exp(-c*z)

print(len(t))

fig = plt.figure(figsize=(7, 10)) 
ax = plt.subplot()
ax.semilogx(dtn,z, linewidth=3)
#plt.title('semilogy')
ax.grid(b=True,which='major', color='k', linestyle='-')
ax.grid(b=True,which='minor', color='0.65', linestyle='-')
ax.set_xlim([20,400])
ax.minorticks_on()
ax.invert_yaxis()
ax.xaxis.tick_top()
ax.xaxis.set_major_formatter(ScalarFormatter())
ax.set_xlabel(r'Tansit time ($\mu s/ft$)')
ax.set_ylabel('Depth(ft)')
ax.xaxis.set_label_position('top')
plt.xticks([20,100,200,300,400])
plt.show()
