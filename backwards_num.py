#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Nov. 7, 2022
# a program reverses the order of a number


def main():
    # variables
    user_num = input("Please enter any number: ")
    is_not_valid = True
    num_reversed = ""
    each_digit = []

    # exception handling
    while is_not_valid:
        # tries turning user input from sting to int
        try:
            int(user_num)

        # if user num is not an int
        except Exception:
            print(f"{user_num} is not an integer!")
            user_num = input("Please enter any number: ")

        # user num is an int
        else:
            # breaks the loop
            is_not_valid = False

            # putting each digit in a list
            each_digit = list(user_num)

            # reverses the order of the numbers
            for counter_two in range(len(each_digit) - 1, -1, -1):
                print(each_digit[counter_two], end="")
            print()


if __name__ == "__main__":
    main()
