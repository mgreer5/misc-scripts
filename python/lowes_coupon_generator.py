#!/usr/bin/env python
import sys
import argparse
from random import randint

############################################################################
#
#   Find master codes at:
#   https://slickdeals.net/f/9549456-lowe-s-10-15-50-off-online-coupons-sharing-only-no-off-topic
#   
#   Or google "lowes coupon master {month} {year}"
#   Example: lowes coupon master may 2018
#
############################################################################

NUM_OF_CODES = 10


def fifteen_off(master_code, coupon_count=1):
    """
    Function to produce coupon codes based on a master code

    Args:
        master_code: (str): master code to use for generation
        coupon_count: (int): number of coupon codes to generate

    Returns:
        console print output of coupon codes
    """
    master_code = '{0:04d}'.format(master_code)
    print(master_code)
    for x in range(coupon_count):
        i = randint(0, 50000)
        add_check_digit("47000" + "%05d" % i + str(master_code))


def add_check_digit(id_without_check_digit):
    check_digit = 0

    for x in range(len(id_without_check_digit)):
        if x % 2 == 0:
            check_digit += int(id_without_check_digit[x])
        else:
            check_digit += int(id_without_check_digit[x]) * 3
            
    print(str(id_without_check_digit) + str((10 - (check_digit % 10)) % 10))


def parse_args(args):
    """
    :param args: arguments passed from the command line.
    :return: return parser object
    """
    parser = argparse.ArgumentParser(description="Lowe's Coupon Generator")
    parser.add_argument("mastercode", help="[mastercode]")
    return parser.parse_args(args)


def main():
    """
    main entry point for commandline application
    """
    try:
        parser = parse_args(sys.argv[1:])
    except SystemExit:
        sys.exit(1)

    if not parser.mastercode:
        print "mastercode is not provided."
        sys.exit(1)

    try:
        master_code = int(parser.mastercode)
    except ValueError:
        print "\"%s\" is not a valid input.\nPlease input 4 numeric digits\n" % parser.mastercode
        sys.exit(1)

    fifteen_off(master_code, NUM_OF_CODES)

if __name__ == '__main__':
    main()
