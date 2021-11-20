# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

#step1 - Create a program that ask 4 numbers. 
num_1= (float(input("Enter your FIRST number here: ")))
num_2= (float(input("Enter your SECOND number here: ")))
num_3= (float(input("Enter your THIRD number here: ")))
num_4= (float(input("Enter your FOURTH number here: " )))

#step2 - Sort the numbers from highest to lowest using only if-else statement.
def highest_num (Qnty_1, Qnty_2, Qnty_3, Qnty_4):
    if Qnty_1 >= Qnty_2 and Qnty_1 >= Qnty_3 and Qnty_1 >= Qnty_4:
        if Qnty_2 >= Qnty_3 and Qnty_2 >= Qnty_4:
            if Qnty_3 >= Qnty_4:
                number_order= [Qnty_1, Qnty_2, Qnty_3, Qnty_4]
                print(f" The following set of numbers are in highest to lowest order. ")
                
