#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: Nov. 7, 2022
# a program reverses the order of a number


def play_again():
    while True:
        # getting user input
        replay = input("Would you like like run this program again? [y/n] ")

        # if user want to rerun the program
        if replay == "y":
            return True

        # if user doesn't want to rerun the program
        elif replay == "n":
            return False

        # user didn't have a valid input
        else:
            print("Input Invalid! Please enter either y or n!")

def main():
    # variables
    each_digit = []

    while True:
        # get user input
        user_num = input("Please enter any number: ")

    # exception handling
        try:
            int(user_num)

        # if user num is not an int
        except Exception:
            print(f"{user_num} is not an integer!")

        # user num is an int
        else:

            # putting each digit in a list
            each_digit = list(user_num)

            # reverses the order of the numbers
            for counter in range(len(each_digit) - 1, -1, -1):
                print(each_digit[counter], end="")
            print()

        if play_again():
            continue
        else:
            break


if __name__ == "__main__":
    main()
