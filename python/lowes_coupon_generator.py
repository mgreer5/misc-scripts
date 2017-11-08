#!/usr/bin/env python
from random import randint

MASTER_CODE = "0017"
NUM_OF_CODES = 10

"""
Function to produce coupon codes based on a master code

Args:
    master_code: (str): master code to use for generation
    coupon_count: (int): number of coupon codes to generate

Returns:
    console print output of coupon codes
"""
def fifteen_off(master_code="0001", coupon_count=1):
    for x in range(coupon_count):
        i = randint(0, 50000)
        add_check_digit("47000" + "%05d" % i + master_code)

def add_check_digit(id_without_check_digit):
    check_digit = 0

    for x in range(len(id_without_check_digit)):
        if x % 2 == 0:
            check_digit += int(id_without_check_digit[x])
        else:
            check_digit += int(id_without_check_digit[x]) * 3
            
    print(str(id_without_check_digit) + str((10 - (check_digit % 10)) % 10))

if __name__ == '__main__':
    fifteen_off(MASTER_CODE, NUM_OF_CODES)