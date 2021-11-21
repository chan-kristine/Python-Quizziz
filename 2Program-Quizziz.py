# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)


from random import randrange
import math

#global list of variables
max_info = 1 # maximum information of user input item
max_items = 10 # total items for the Quiz
correctanswer = 0 # worrect answers of the user
wronganswer = 0 # wrong answers of the user 

progintro = print("Welcome to Aleja's BrainyMath! This mathematics addition game will presumably examine your brain within random digits ranging from 0-99.")
Username = input("Kindly enter you First Name below before we proceed to the Quiz: ")
ryready = input(f"Hi {Username.title()}! Are you ready for the Math Quiz? (Respond: Yes or No): ")
Ready_ = False

# ADDING Condition Statement.
while not Ready_:
    if ryready.replace(".","",10).title() == "Yes" or ryready.replace("!","",10).title() == "Yes":
        ryready = "Yes"
        Ready_ = True
    while ryready.replace(".","",10).title() != "Yes":
        if ryready.replace(".","",10).title() or ryready.replace("!","",10).title() == "No":
            ryready = input(f"(Okay, take your time {Username} 😄/ Now, are you ready to start the quiz {Username}? (Respond: Yes or No:  ")
            if ryready.replace(".","",10).title() == "No" or ryready.replace("!","",10).title() == "No":
                ryready = "No"
              