# Copyright 2019 MIT Rocket Team
#!/usr/bin/python3

import sys, getopt


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

if __name__ == "__main__":
    main(sys.argv[1:])
