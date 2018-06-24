import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter



z = np.arange(100,13000,100) # depth
z2 = np.arange(5000,10000,500) # depth

dtm= 70
dtml = 200
c = 0.000245

dtn= dtm + (dtml - dtm)*np.exp(-c*z)


def pore_pressure_plot(z,obg, pp, z2, rft, labels=['OBG', 'Pp DT', 'RFT']):
    """TODO: Docstring for pore_pressure_plot.

    :z: depth
    :obg: overburden gradient
    :pp: pore pressure
    :rft: rft pressure
    :label: TODO
    :returns: TODO

    """

    fig = plt.figure(figsize=(7, 10)) 
    ax = plt.subplot()
    ax.plot(obg,z, linewidth=3, label=labels[0])
    ax.plot(pp,z, linewidth=3, label=labels[1])
    ax.plot(rft,z2, 'ro', label=labels[2])
    #plt.title('semilogy')
    ax.grid(b=True,which='major', color='0.4', linestyle='-')
    ax.grid(b=True,which='minor', color='0.75', linestyle='-')
    ax.set_xlim([8,obg.max()])
    ax.minorticks_on()
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.xaxis.set_major_formatter(ScalarFormatter())
    ax.set_xlabel(r'Pore pressure gradient ($ppg$)', fontsize=14)
    ax.set_ylabel('Depth(ft)', fontsize=14)
    ax.xaxis.set_label_position('top')
    ax.set_axisbelow(True)
    plt.legend()
    #plt.xticks([20,100,200,300,400])
    plt.show()



if __name__=='__main__':
    pore_pressure_plot(z, 3*z, 2*z, z2,1.5*z2)

#data={'z': z, 'obg':3*z, 'pp':2*z}
