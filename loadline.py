import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# CONSTANTS
TC0 = 9.2 # K
BC20 = 14.5 # T
C0 = 31.4 # T
alpha = 0.63
beta = 1
gamma = 2.3
Jref = 3000 # A/mm^2

def BC2(T):
    result = BC20*(1-(T/TC0)**(1.7))
    return result

def Jc(B,T):
    prod1 = C0/B*(B/BC2(T))**alpha
    prod2 = (1-B/BC2(T))**beta
    prod3 = (1-(T/TC0)**(1.7))**gamma
    return Jref*prod1*prod2*prod3

def getJeng(B,T,factor1,factor2):
    return factor1*factor2*Jc(B,T)

def load(B,Bpeak,Jwork):
    J = Jwork + (B-Bpeak)*Jwork/Bpeak
    return J

def findIntersection(T,Bpeak,Jwork,factor1,factor2,B0):
    return fsolve(lambda B : getJeng(B,T,factor1,factor2) - load(B,Bpeak,Jwork),B0)

def main():
    #fix temperature
    T = 4.2 # K (liquid Helium)
    cable_in_total = 0.08 # A_rutherford cable / A_total (in simulation)
    cond_in_cable = 0.2 # A_SC / A_rutherford cable (alrady summed over N strand)

    # PLOT CRITICAL CURRENT DENSITY
    B = np.arange(0.1,3,0.001)
    Jeng = getJeng(B,T,cable_in_total,cond_in_cable)
    plt.plot(B, Jeng, label = "$J^{eng}_c$ @ 4.2 K")
    plt.xlabel('B [T]')
    plt.ylabel('$J_{eng}$ [A/mm$^2$]')
    plt.title('KLOE magnet loadline')

    # PLOT loadline
    # the work point is specified by
    B_peak = 0.6088 #0.738 # T
    J_work = 50.912 #58.04 # A/mm^2
    plt.plot(B,load(B,B_peak,J_work), label = "loadline")

    # find intersection bewteen loadline and Jc
    start = 0.1
    B_inter = findIntersection(T,B_peak,J_work,cable_in_total,cond_in_cable,start)
    J_inter = load(B_inter,B_peak,J_work)

    print("The intersection is {},{}".format(B_inter,J_inter))

    # PLOT work point and intersection
    plt.plot(B_peak,J_work,"ro")
    plt.plot(B_inter,J_inter,"ro")

    #compute MARGIN
    perc = 100*B_peak/B_inter
    print("B peak is at {} %".format(perc))
    margin = 100-perc
    print("The work point margin is then {}".format(margin))

    # function to show the plot
    plt.legend()
    plt.show()

main()
