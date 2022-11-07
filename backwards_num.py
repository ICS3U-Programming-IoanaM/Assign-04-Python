#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Nov. 7, 2022
# a program reverses the order of a number


def main():
    # variables
    user_num_string = input("Please enter any number: ")
    user_num_int = 0
    is_not_valid = True

    # exception handling
    while is_not_valid:
        # tries turning user input from sting to int
        try:
            user_num_int = int(user_num_string)

        # if user num is not an int
        except Exception:
            print(f"{user_num_string} is not an integer!")
            user_num_string = input("Please enter any number: ")

        # if user num is an int
        else:
            is_not_valid = False

if __name__ == "__main__":
    main()