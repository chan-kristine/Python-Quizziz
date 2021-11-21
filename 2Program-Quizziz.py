# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)


from random import randrange
import math

# GLOBAL VARIABLES LIST
max_info = 1 # maximum information of user input item
max_items = 10 # total items for the Quiz
correctanswer = 0 # worrect answers of the user
wronganswer = 0 # wrong answers of the user 

progintro = print("Welcome to Aleja's BrainyMath! This mathematics addition game will presumably examine your brain within random digits ranging from 0-99.")
Username = input("Kindly enter you First Name below before we proceed to the Quiz:")
ryReady = input(f"Hi {Username.title()}! Are you ready for the Math Quiz? (Respond: Yes or No)")
ready = False
