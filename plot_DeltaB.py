import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def read(file):
    x = []
    y = []

    while True:
        line = file.readline()
        if not line:
            break
        values = line.split()
        x.append(float(values[0]))
        y.append(float(values[1]))

    file.close()
    return x, y

def main():
    file_simu1 = open("sim/Bz_vs_z_at_r_0_simu_forDelta.txt", "r")
    file_simu2 = open("sim/Bz_vs_z_at_r_7,5_simu.txt", "r")
    file_real = open("data/DeltaBz_vs_z.dat","r")

    x_simu1 = []
    x_simu2 = []
    x_real = []
    B_simu1 = []
    B_simu2 = []
    deltaB_real = []

    x_simu1, B_simu1 = read(file_simu1) # this is cm vs T
    x_simu2, B_simu2 = read(file_simu2)
    x_real, deltaB_real = read(file_real) #this is cm vs Gauss

    x_simu1 = np.asarray(x_simu1)
    x_simu2 = np.asarray(x_simu2)
    x_real = np.asarray(x_real)
    B_simu1 = np.asarray(B_simu1)
    B_simu2 = np.asarray(B_simu2)
    deltaB_real = np.asarray(deltaB_real)

    x_simu1 = x_simu1 - 200
    x_simu2 = x_simu2 - 200

    #x_simu = x_simu - 200  #offset: coordinates are read on the line

    ##CHANGE EVERYTHING TO cm vs TESLA
    x_real = x_real/10
    deltaB_real = deltaB_real/10000  # 1 G = 10^-4 T

    #find max
    #maximum = max(B_real)
    #print("Peak field value is {}".format(maximum))

    #B_simu = B_simu - 0.025*B_simu

    plt.plot(x_simu1,B_simu1-B_simu2, label = "simulation")
    plt.plot(x_real,deltaB_real, "ro", label = "KLOE data")

    plt.axis([-200, 200, -0.02, 0.02]) #0 200 0.54 0.63
    plt.xlabel('z [cm]')
    plt.ylabel('$\Delta B_z$ [T]')
    plt.title('$B_z(r=0)-B_z(r=7.5 cm)$ vs $z$')
    plt.rcParams['legend.numpoints'] = 1

    plt.legend()
    plt.show()

main()
