# Copyright 2019 MIT Rocket Team
#!/usr/bin/python3

import sys, getopt
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

def set_3d_cone():
    """Equation of a cone used for rocket team cone
    (x-a)^2 + (y-b)^2 = ((z-c)R)^2 where a,b,c is the vertex
    """
    # Constants
    n_angles = 30
    radii = 12  # units of [cm]
    angles = np.array(np.linspace(0, 360, n_angles)) * np.pi / 180
    # Create a circle
    x = np.append(0, (radii*np.cos(angles)))
    y = np.append(0, (radii*np.sin(angles)))
    z = np.zeros(len(x))
    # Set the tip
    x[0] = 0
    y[0] = 0
    z[0] = 1
    print(radii)
    print(angles)
    print(x)
    print(y)
    print(z)
    # Color mapping
    levels = np.append(0, random.random()*radii*np.cos(angles))
    print(levels)
    print(len(x)); print(len(levels))
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(x, y, z, cmap=levels, linewidth=0.2, antialiased=True)
    plt.show()


def set_mayavi_mesh():
    """Mayavi Test
    """
    pass


def get_datalog(input_file: str):
    pass


def print_datalog(input_file: str):
    logged_data = open(input_file, "r")
    with open(input_file, 'r') as log:
        data = log.read()
        print(data)


def main(argv):
    input_file = "../datalogs/DATALOG.TXT"
    output_file = ""
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('nc-thermal.py -i <input_file> -o <output_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('nc-thermal.py -i <input_file> -o <output_file>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
    print('Input file is "', input_file)
    print('Output file is "', output_file)

    data = get_datalog(input_file);
    set_3d_cone()


if __name__ == "__main__":
    main(sys.argv[1:])
