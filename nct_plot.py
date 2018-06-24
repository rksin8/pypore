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

def nct_plot(z1, dtn1, z2, dtn2, labels=['DT normal', 'DT shale']):
    """TODO: Docstring for nct_plot.

    :z1: TODO
    :dt1: TODO
    :z2: TODO
    :dt2: TODO
    :labels: TODO
    :'DT shale']: TODO
    :returns: TODO

    """
    pass
    xmax= np.max([dtn1.max(),dtn2.max()])//100 +200

    fig = plt.figure(figsize=(7, 10)) 
    ax = plt.subplot()
    ax.set_xscale('log')
    ax.plot(dtn1,z1, linewidth=2, label=labels[0])
    ax.plot(dtn2,z2, linewidth=2, label=labels[1])
    #plt.title('semilogy')
    ax.set_xlim([20,xmax])
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.xaxis.set_major_formatter(ScalarFormatter())
    ax.set_xlabel(r'Tansit time ($\mu s/ft$)', fontsize=14)
    ax.set_ylabel('Depth(ft)',fontsize=14)
    ax.xaxis.set_label_position('top')
    plt.xticks([20,100,200,300,400])
    plt.legend(loc='upper left')
    plt.grid(b=True,which='major', color='0.4', linestyle='-')
    plt.grid(b=True,which='minor', color='0.75', linestyle='-')
    plt.minorticks_on()
    ax.set_axisbelow(True)
    plt.show()


if __name__ == '__main__':
    nct_plot(z, dtn, z, 15+dtn)

