#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Mon,Apr26/2021
# This program calculates the volume of a rectangular prism


def main():
    # status:
    print("we will be calculating the volume of a rectangular prism :")
    # input:
    length_of_prism = int(input("Enter the Length (cm):"))
    width_of_prism = int(input("Enter the width (cm):"))
    Height_of_prism = int(input("Enter the height (cm):"))
    # process:
    volume = length_of_prism * width_of_prism * Height_of_prism
    # output:
    print("")
    print("Volume is {} cm3".format(volume))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
