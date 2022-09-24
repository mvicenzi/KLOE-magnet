import statistics as stat
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def main():
    file = open("B_at_PM.dat", "r")

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

        select = [205,215,225,235,240,245]

        if count != 0:
            values = line.split()
            #print(values)
            if float(values[1]) in select:
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
    Bz = np.asarray(Bz)
    Br = np.asarray(Br)

    theta = 180/3.14*np.arctan(Br/Bz)

    plt.plot(z,theta,"ro")

    plt.axis([200, 250, -20, 15])
    plt.xlabel('z [cm]')
    plt.ylabel('Angle [°]')
    plt.title('Angle vs $z$ with $r$ in $[200,226]$ cm')

    #plt.rcParams['legend.numpoints'] = 1
    #plt.legend()

    plt.show()

main()
