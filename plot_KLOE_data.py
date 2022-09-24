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
    file_data0 = open("data/Bz_vs_z_at_r_0.dat","r")
    file_data1 = open("data/Bz_vs_z_at_r_19,5.dat","r")
    file_data2 = open("data/Bz_vs_z_at_r_49,5.dat","r")
    file_data3 = open("data/Bz_vs_z_at_r_129,5.dat","r")

    x_0 = []
    x_1 = []
    x_2 = []
    x_3 = []
    B_0 = []
    B_1 = []
    B_2 = []
    B_3 = []

    x_0, B_0 = read(file_data0) #this is cm vs Gauss
    x_1, B_1 = read(file_data1) #this is mm vs Gauss
    x_2, B_2 = read(file_data2) #this is mm vs Gauss
    x_3, B_3 = read(file_data3) #this is mm vs Gauss

    x_0 = np.asarray(x_0)
    x_1 = np.asarray(x_1)
    x_2 = np.asarray(x_2)
    x_3 = np.asarray(x_3)
    B_0 = np.asarray(B_0)
    B_1 = np.asarray(B_1)
    B_2 = np.asarray(B_2)
    B_3 = np.asarray(B_3)

    ##CHANGE EVERYTHING TO cm vs TESLA
    x_0 = x_0
    B_0 = B_0/10000  # 1 G = 10^-4 T
    x_1 = x_1/10
    B_1 = B_1/10000  # 1 G = 10^-4 T
    x_2 = x_2/10
    B_2 = B_2/10000  # 1 G = 10^-4 T
    x_3 = x_3/10
    B_3 = B_3/10000  # 1 G = 10^-4 T

    plt.plot(x_0,B_0, "ro", label = "$r=0\,cm$")
    plt.plot(x_1,B_1, "bv", label = "$r=19.5\,cm$")
    plt.plot(x_2,B_2, "gs", label = "$r=49.5\,cm$")
    plt.plot(x_3,B_3, "y^", label = "$r=129.5\,cm$")

    plt.axis([0, 360, 0, 0.7]) #0 200 0.54 0.63
    plt.xlabel('r [cm]')
    plt.ylabel('$B_z$ [T]')
    plt.title('KLOE data')
    plt.rcParams['legend.numpoints'] = 1

    plt.legend()
    plt.show()

main()
