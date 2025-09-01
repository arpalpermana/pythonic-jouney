# This is Basic Function Exercise

import os


def header():
    """Header of program function"""
    os.system("clear")
    print(f"{'CALCULATE AREA': ^30}")
    print(f"{'AND PERIMETER': ^30}")
    print(f"{'*'*40: ^30}")


def input_user():
    """Input user function"""
    width = int(input("Input width \t\t: "))
    length = int(input("Input length \t\t: "))

    return width, length


def calculate_area(width, length):
    """Calculate area function"""
    return width * length


def calculate_perimeter(width, length):
    """Calculate perimeter function"""

    return 2 * (width + length)


def main():
    while True:
        header()

        option = int(
            input(
                f"Choose 1 for area \nChoose 2 for Perimeter \nChoose 3 for both \nYour option? \t"
            )
        )
        width, length = input_user()

        area = calculate_area(width, length)
        perimeter = calculate_perimeter(width, length)

        if option == 1:
            print(f"Area of rectangle \t= {area}")
        elif option == 2:
            print(f"Perimeter of rectangle \t= {perimeter}")
        else:
            print(f"Area of rectangle \t= {area}")
            print(f"Perimeter of rectangle \t= {perimeter}")

        while True:
            isContinue = input("\nDo you want to continue? (y/n) \t: ").lower()
            if isContinue == "n":
                print("Program is shutdown.")
                return
            elif isContinue == "y":
                break
            else:
                print("Please Input with y or n")


main()
