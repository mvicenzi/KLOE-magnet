import statistics as stat
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def main():
    file = open("B_field_DC.dat", "r")

    r = []
    z = []
    B = []
    Br = []
    Bz = []

    count = 0

    while True:

        # Get next line from file
        line = file.readline()

        # if line is empty
        # end of file is reached
        if not line:
            break

        if count != 0:
            values = line.split()
            #print(values)
            r.append(float(values[0]))
            z.append(float(values[1]))
            B.append(float(values[2]))
            Br.append(float(values[3]))
            Bz.append(float(values[4]))

        count += 1

    file.close()

    #find max value
    maximum = max(B)
    maximum_Bz = max(Bz)
    maximum_Br = max(Br)
    print("B peak value: {} \nBz peak value: {} \nBr peak value: {}".format(maximum, maximum_Bz, maximum_Br))

    #find mean/median value
    mean = stat.mean(B)
    mean_Bz = stat.mean(Bz)
    mean_Br = stat.mean(Br)
    print("mean B: {} \nmean Bz: {} \nmean Br: {}".format(mean,mean_Bz,mean_Br))

    median = stat.median(B)
    median_Bz = stat.median(Bz)
    median_Br = stat.median(Br)
    print("median B: {} \nmedian Bz: {} \nmedian Br: {}".format(median,median_Bz,median_Br))

    r = np.asarray(r)
    z = np.asarray(z)
    B_1d = np.asarray(B)

    #B_1d = B_1d - 0.015

    #print(B_1d)
    B_2d = np.reshape(B_1d,(-1,201))  # le righe (quindi r)
    #print(B_2d)
    #print(B_2d[:,0])
    #plt.hist2d(r,z, weights = B_1d, cmap = cm.viridis)
    plt.contourf(B_2d, extent=(np.amin(r), np.amax(r), np.amax(z), np.amin(z)), cmap=cm.viridis)
    plt.colorbar()
    plt.show()

main()
