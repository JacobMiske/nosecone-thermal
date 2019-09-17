# Copyright 2019 MIT Rocket Team
#!/usr/bin/python3

import sys
import getopt
import os
import cmd
import matplotlib
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import getpass
# from manual import ManualNosecone
# from auto import AutoNosecone
import matplotlib.cm as cmx
from mpl_toolkits.mplot3d import Axes3D
import pyfiglet

my_path = os.path.abspath(__file__)  # Figures out the absolute path


class NCThermal(cmd.Cmd):
    """A simple cmd application using cmd.
    """
    custom_fig = pyfiglet.Figlet(font='slant')
    intro = 'Welcome to the NC Thermal shell.  Type help or ? to list commands.\n'
    prompt = '> '
    file = None
    print(custom_fig.renderText('  NC Thermal'))

    def do_status(self, arg):
        """status: Yields device status for the edge device.
        Returns a table of details related to health of NC Thermal unit.
        """
        def status():
            """Runs the list generation
            """
            custom_fig = pyfiglet.Figlet(font='slant')
            print(custom_fig.renderText(' status'))
        status()

    def do_whoami(self, arg):
        """Prints out user data
        """
        def whoami():
            print(getpass.getuser())
            print('File Directory')
            cwd = os.getcwd()  # Get the current working directory (cwd)
            files = os.listdir(cwd)  # Get all the files in that directory
            print("Files in '%s': %s" % (cwd, files))
        whoami()

    def do_run_sim(self, arg):
        """
        Runs the manual or automatic simulation
        :return:
        """
        def scatter3d(x, y, z, cs, colorsMap="jet"):
            cm = plt.get_cmap(colorsMap)
            cNorm = matplotlib.colors.Normalize(vmin=min(cs), vmax=max(cs))
            scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
            fig = plt.figure()
            ax = Axes3D(fig)
            ax.scatter(x, y, z, c=scalarMap.to_rgba(cs))
            scalarMap.set_array(cs)
            fig.colorbar(scalarMap)
            plt.title("Temperatures at points across structure")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.savefig("assets/temperature_scatter.png")
            plt.show()

        def get_constraints(mat: str):
            """For materials on nosecone, figure out softening temps
            :param: mat is a string which is the name of the nosecone material
            :return: breaking temp where material falls apart (50% strength point)
            """
            breaking_temp = 0
            fg_breaking_temp = 371  # [degrees C] of 700 degrees F
            if (mat == "fiberglass"):
                breaking_temp = fg_breaking_temp
            return breaking_temp

        def set_3d_cone():
            """Equation of a cone used for rocket team cone
            (x-a)^2 + (y-b)^2 = ((z-c)R)^2 where a,b,c is the vertex
            """
            # Constants
            n_angles = 30
            radii = 12  # units of [cm]
            angles = np.array(np.linspace(0, 360, n_angles)) * np.pi / 180
            # Create a circle
            x = np.append(0, (radii * np.cos(angles)))
            y = np.append(0, (radii * np.sin(angles)))
            z = np.zeros(len(x))
            # Set the tip
            x[0] = 0
            y[0] = 0
            z[0] = 1
            # Color mapping
            levels = np.append(0, random.random() * radii * np.cos(angles))
            fig = plt.figure()
            ax = fig.gca(projection='3d')
            ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)
            plt.title("Nosecone Geometry")
            plt.show()

        def set_mayavi_mesh():
            """Mayavi Test
            Not configured yet as still looking into documentation.
            """
            pass

        while True:
            try:
                manual_choice = int(
                    input("Run a test with input files or manually assign values? (0=inputs, 1=manual)"))
                break
            except ValueError:
                print("Did not compute, please try and again...")

        if manual_choice == 0:
            try:
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
            except BaseException:
                print("Sorry, input files were not parsed")

        if manual_choice == 1:
            set_3d_cone()
            scatter3d([1, 5, 2], [2, 4, 4], [1, 2, 1], [1.2, 2.5, 3])

    def do_bye(self, arg):
        """Stop cmd, close the window, and exit:  BYE
        """
        print("Thank you for using NC Thermal")
        self.close()
        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


def main(argv):
    """Main Function
    :param: argv
    """
    print("NC Thermal is a nosecone thermal analysis tool for MIT Rocket Team \n")
    c = NCThermal()
    sys.exit(c.cmdloop())


if __name__ == "__main__":
    main(sys.argv[1:])
