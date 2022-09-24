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
    file_simu = open("B_on_diameter_long_simu.txt", "r")
    file_real = open("../KLOE_data/Bz_vs_r_at_z_0.dat","r")

    x_simu = []
    x_real = []
    B_simu = []
    B_real = []

    x_simu, B_simu = read(file_simu) # this is cm vs T
    x_real, B_real = read(file_real) #this is cm vs Gauss

    x_simu = np.asarray(x_simu)
    x_real = np.asarray(x_real)
    B_simu = np.asarray(B_simu)
    B_real = np.asarray(B_real)

    #x_simu = x_simu - 200  #offset: coordinates are read on the line

    ##CHANGE EVERYTHING TO cm vs TESLA
    x_real = x_real/10
    B_real = B_real/10000  # 1 G = 10^-4 T

    #find max
    maximum = max(B_real)
    print("Peak field value is {}".format(maximum))

    #B_simu = B_simu - 0.025*B_simu

    plt.plot(x_simu,B_simu, label = "simulation")
    plt.plot(x_real,B_real, "ro", label = "KLOE data")

    #plt.axis([331, 700, -1e-03, 0]) #0 200 0.54 0.63
    plt.xlabel('r [cm]')
    plt.ylabel('$B_z$ [T]')
    plt.title('$B_z$ vs $r$ at $z=0\,cm$')
    plt.rcParams['legend.numpoints'] = 1

    plt.legend()
    plt.show()

main()
