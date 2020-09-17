"""
Name: Omar Aljaloud
Email: oaa3024@rit.edu
Description: This is a Distraction tool that will be used to distract blue teamers from protecting their machines.
"""

import os
import keyboard
import string
import time
import sys
import argparse

# A list that contains all the keyboard characters
KEYS = list(string.printable)

def keyClear():
    """
    This function will monitor the keys clicked in the keyboard and with each key clicked,
    it will clear the terminal.
    """
    global KEYS
    while True:
        # Read the keyboard clicks
        key = keyboard.read_key()
        if key == '1':
            break
        if key in KEYS:
            # Clear the terminal
            os.system("clear")
            time.sleep(1)


def keyAdd():
    """
    This function will monitor the keys clicked in the keyboard and with each key clicked,
    it will type the same key multiple times in the terminal.
    """
    global KEYS
    while True:
        # Read the keyboard clicks
        key = keyboard.read_key()
        if key == '1':
            break
        if key in KEYS:
            # Add the same litter in the terminal multiple times.
            keyboard.write(key*2)
            time.sleep(0.1)


def keyWrite():
    """
    This function will monitor the keys clicked in the keyboard and with each key clicked,
    it will write a short paragraph(maybe for now it will print O72_is_here) in the terminal.
    """

    global KEYS
    while True:
        key = keyboard.read_key()
        if key == '1':
            break
        if key in KEYS:
            # Clear the terminal
            os.system("echo O72_is_here")
            time.sleep(1)

def arg_parser():
    """
    This function gets the inputs from the user to use them in the tools
    :return: the Namespace of the input arguments.
    """
    parser = argparse.ArgumentParser(prog='ezDistract.py', usage='%(prog)s [options]')
    options = parser.add_argument_group('Flag options', '')
    options.add_argument('-c', '--clear', action='store_true', help='Clears the terminal as soon as the user click'
                                                                    'any key in the keyboard')
    options.add_argument('-a', '--add', action='store_true', help='Add the same key multiple times in the terminal')
    options.add_argument('-w', '--write', action='store_true', help='Write sentences in terminal as soon as the user'
                                                                    'click any key in the keyboard')

    if len(sys.argv) != 2:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args


def main():
    """
    Read the flag that is given with the tool then it will call the right function.
    """

    args = arg_parser()

    if args.clear:
        keyClear()
    if args.add:
        keyAdd()
    if args.write:
        keyWrite()


if __name__ == "__main__":
    main()
