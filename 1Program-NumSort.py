# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.





# Create a program that ask 4 numbers. 
num1 = float(input("Enter the FIRST number here:"))
num2 = float(input("Enter the SECOND number here: "))
num3 = float(input("Enter the THIRD number here:  "))
num4 = float(input("Enter the FOURTH number here: "))


# Sort the numbers from highest to lowest using only if-else statement.
def highest_num(Qnty_1, Qnty_2, Qnty_3, Qnty_4):

    if Qnty_1 >= Qnty_2 and Qnty_1 >= Qnty_3 and Qnty_1 >= Qnty_4:
        if Qnty_2 >= Qnty_3 and Qnty_2 >= Qnty_4:
            if Qnty_3 >= Qnty_4:
                number_order = [Qnty_1, Qnty_2, Qnty_3, Qnty_4]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
            elif Qnty_4 >= Qnty_3:
                number_order = [Qnty_1, Qnty_2, Qnty_4, Qnty_3]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
        elif Qnty_3 >= Qnty_2 and Qnty_3 >= Qnty_4:
            if Qnty_2 >= Qnty_4:
                number_order = [Qnty_1, Qnty_3, Qnty_2, Qnty_4]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
            elif Qnty_4 >= Qnty_2:
                number_order = [Qnty_1, Qnty_3, Qnty_4, Qnty_2]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
        elif Qnty_4 >= Qnty_2 and Qnty_4 >= Qnty_3:
            if Qnty_3 >= Qnty_2:
                number_order = [Qnty_1, Qnty_4, Qnty_3, Qnty_2]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
            elif Qnty_2 >= Qnty_3:
                number_order = [Qnty_1, Qnty_4, Qnty_2, Qnty_3]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
    elif Qnty_2 >= Qnty_1 and Qnty_2 >= Qnty_3 and Qnty_2 >= Qnty_4:
        if Qnty_1 >= Qnty_3 and Qnty_1 >= Qnty_4:
            if Qnty_3 >= Qnty_4:
                number_order = [Qnty_2, Qnty_1, Qnty_3, Qnty_4]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
            elif Qnty_4 >= Qnty_3:
                number_order = [Qnty_2, Qnty_1, Qnty_4, Qnty_3]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
        elif Qnty_3 >= Qnty_1 and Qnty_3 >= Qnty_4:
            if Qnty_1 >= Qnty_4:
                number_order = [Qnty_2, Qnty_3, Qnty_1, Qnty_4]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
            elif Qnty_4 >= Qnty_1:
                number_order = [Qnty_2, Qnty_3, Qnty_4, Qnty_1]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
        elif Qnty_4 >= Qnty_1 and Qnty_4 >= Qnty_3:
            if Qnty_1 >= Qnty_3:
                number_order = [Qnty_2, Qnty_4, Qnty_1, Qnty_3]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
            elif Qnty_3 >= Qnty_1:
                number_order = [Qnty_2, Qnty_4, Qnty_3, Qnty_1]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
    elif Qnty_3 >= Qnty_1 and Qnty_3 >= Qnty_2 and Qnty_3 >= Qnty_4:
        if Qnty_1 >= Qnty_2 and Qnty_1 >= Qnty_4:
            if Qnty_2 >= Qnty_4:
                number_order = [Qnty_3, Qnty_1, Qnty_2, Qnty_4]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
            elif Qnty_4 >= Qnty_2:
                number_order = [Qnty_3, Qnty_1, Qnty_4, Qnty_2]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
        elif Qnty_2 >= Qnty_1 and Qnty_2 >= Qnty_4:
            if Qnty_1 >= Qnty_4:
                number_order = [Qnty_3, Qnty_2, Qnty_1, Qnty_4]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
            elif Qnty_4 >= Qnty_1:
                number_order = [Qnty_3, Qnty_2, Qnty_4, Qnty_1]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
        elif Qnty_4 >= Qnty_1 and Qnty_4 >= Qnty_2:
            if Qnty_1 >= Qnty_2:
                number_order = [Qnty_3, Qnty_4,Qnty_1, Qnty_2]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
            elif Qnty_2 >= Qnty_1:
                number_order = [Qnty_3, Qnty_4, Qnty_2, Qnty_1]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
    elif Qnty_4 >= Qnty_1 and Qnty_4 >= Qnty_2 and Qnty_4 >= Qnty_3:
        if Qnty_1 >= Qnty_2 and Qnty_1 >= Qnty_3:
            if Qnty_2 >= Qnty_3:
                number_order = [Qnty_4, Qnty_1, Qnty_2, Qnty_3]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
            elif Qnty_3 >= Qnty_2:
                number_order = [Qnty_4, Qnty_1, Qnty_3, Qnty_2]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
        elif Qnty_2 >= Qnty_1 and Qnty_2 >= Qnty_3:
            if Qnty_1 >= Qnty_3:
                number_order = [Qnty_4, Qnty_2, Qnty_1, Qnty_3]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
            elif Qnty_3 >= Qnty_1:
                number_order = [Qnty_4, Qnty_2, Qnty_3, Qnty_1]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
        elif Qnty_3 >= Qnty_1 and Qnty_3 >= Qnty_2:
            if Qnty_1 >= Qnty_2:
                number_order = [Qnty_4, Qnty_3, Qnty_1, Qnty_2]
                print(f"The following set of numbers is in highest to lowest order {number_order}")
            elif Qnty_2 >= Qnty_1:
                number_order = [Qnty_4, Qnty_3, Qnty_2, Qnty_1]
                print(f"The following set of numbers is in highest to lowest order {number_order}")

highest_num(num1, num2, num3, num4)

    