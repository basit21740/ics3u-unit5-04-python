#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Jan 2022
# This program calculates the volume of a cylinder

import math


def cylinder_volume(radius, height):
    # This function calculates the volume of a cylinder

    # process
    volume = math.pi * (radius * radius) * height

    return volume


def main():
    # this function receives input
    print("This program calculates the volume of a cylinder")
    print("")

    # input
    while True:
        try:
            radius_input = input("Enter the radius (cm): ")
            radius_int = int(radius_input)
            height_input = input("Enter the height (cm): ")
            height_int = int(height_input)
            print("")

            if radius_int > 0 and height_int > 0:
                # call function
                cylinder = cylinder_volume(radius_int, height_int)

                volume_rounded = "{0:.4g}".format(cylinder)

                print(
                    "The volume of cylinder with a radius of {0} cm and a"
                    " height of {1} cm is {2} cm².".format(
                        radius_int, height_int, volume_rounded
                    )
                )
                print("\nDone")
                break
            else:
                # output
                print("Enter a positive integer for both values, try again.")
                print("")

        except Exception:
            # output
            print("Enter a number for both values, try again.")


if __name__ == "__main__":
    main()
