# Copyright 2019 MIT Rocket Team
#!/usr/bin/python3

import sys, getopt
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


class ManualNosecone:
    """A manually configured nosecone
    """

    def get_datalog(self, input_file: str):
        pass


    def print_datalog(self, input_file: str):
        logged_data = open(input_file, "r")
        with open(input_file, 'r') as log:
            data = log.read()
            print(data)