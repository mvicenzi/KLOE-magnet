def main():
    file = open("sim/B_field_map_conductor.dat", "r")

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
            r.append(values[0])
            z.append(values[1])
            B.append(values[2])
            Br.append(values[3])
            Bz.append(values[4])

        count += 1

    file.close()

    #find max
    maximum = max(B)
    print("Peak field value is {}".format(maximum))

main()
