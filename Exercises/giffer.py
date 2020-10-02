''' This module takes multiple images and giffifys them through command line
arguments
'''

from pathlib import Path
from pygifsicle import optimize
import imageio
import os
import sys, getopt

# Guides used for this script: https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# and: https://medium.com/swlh/python-animated-images-6a85b9b68f86

CURRENT_WORKING_DIR = os.getcwd()


def giffer(image_folder, output_folder, output_file):
    image_path = Path(image_folder)
    images = list(image_path.glob('*.png'))
    image_list = [imageio.imread(file_name) for file_name in images]

    gif_path = output_folder + output_file

    imageio.mimwrite(gif_path, image_list, duration=3 ,fps=100)


def main(argv):
    image_folder = CURRENT_WORKING_DIR
    output_dir = image_folder + '/gif_output/' # output directory

    try:
        opts, args = getopt.getopt(argv, "ho:",["-help","-output="])

    except getopt.GetoptError:
        print("Error!")
        print('giffer.py -o <output gif>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h': # help flag
            print ('giffer.py -o <output gif>')
            sys.exit()

        elif opt in ('-o','--output'): # check for output flag
            name = arg

            if os.path.isdir(output_dir): # check if output directory exists
                giffer(image_folder, output_dir, name)

            else: # if output directory does not exist, ask if user allows its creation
                choice = input("Make output directory " + output_dir +" (Y/N)?").upper()

                while choice not in ('N','Y'):
                    print("Invalid choice.")
                    choice = input("Make output directory " + output_dir + " (Y/N)?")

                if choice == 'Y':
                    os.mkdir(output_dir)
                    giffer(image_folder, output_dir, name)
                else:
                    sys.exit()

    print("Completed")


if __name__ == "__main__":
    main(sys.argv[1:])
