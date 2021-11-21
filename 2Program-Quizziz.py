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
progintro = print("Welcome to Aleja's BrainMath Quiz! This mathematics addition game will presumably examine your brain within random digits ranging from 0-99.")
Username = input("Kindly enter you First Name below before we proceed to the Quiz: ")
ryready = input(f"Hi {Username.title()}! Are you ready for the Math Quiz? (Respond: Yes or No): ")
Ready_ = False

# Adding Statement Conditions
while not Ready_:
    if ryready.replace(".","",10).title() == "Yes" or ryready.replace("!","",10).title() == "Yes":
        ryready = "Yes"
        Ready_ = True
    while ryready.replace(".","",10).title() != "Yes":
        if ryready.replace(".","",10).title() or ryready.replace("!","",10).title() == "No":
            ryready = input(f"Okay, take your time {Username} 😄/ Now, are you ready to start the quiz {Username}? (Respond: Yes or No):  ")
            if ryready.replace(".","",10).title() == "No" or ryready.replace("!","",10).title() == "No":
                ryready = "No"
                break
            elif ryready.replace(".","",10).title() == "Yes" or ryready.replace("!","",10).title() == "Yes":
                ryready = "Yes"
                break
            while ryready.replace(".","",10).title() != "Yes":
                ryready = input(f"\nSorry,Python 3.0 didn't understand your response! ☹️\nAre you now ready for the BrainyMath Quiz {Username} (Respond: Yes or No ")
                if ryready.upper() in "BCDFGHJKLMNPQRSTVWXYZAEIOU":
                    ryready = input(f"\nSorry, Python 3.0 didn't understand your response! ☹️\nAre you now ready for the BrainyMath Quiz {Username} (Respond: Yes or No ")
                elif ryready.replace(".","",10).title() == "No" or ryready.replace("!","",10).title() == "No":
                    ryready = "No"
                    break
                elif ryready.replace(".","",10).title() == "Yes" or ryready.replace("!","",10).title() == "Yes":
                    ryready = "Yes"
                    break
                else:
                    ryready = "C"
        else:
            ryready = input(f"\n\033[0mPython 3.0 didn't understand your response, sorry! ☹️\nAre you now ready for the \033[32;1mMath Quiz\33[0m? (Respond: \33[34;1mYes\33[0m or \33[34;1mNo\33[0m)\n\033[32;1m>>>\33[0m\33[34;1m ")
            if ryready.upper() in "BCDFGHJKLMNPQRSTVWXYZAEIOU":
                ryready = input(f"\n\033[0mPython 3.0 didn't understand your response, sorry! ☹️\nAre you now ready for the \033[32;1mMath Quiz\33[0m? (Respond: \33[34;1mYes\33[0m or \33[34;1mNo\33[0m)\n\033[32;1m>>>\33[0m\33[34;1m ")
            elif ryready.replace(".","",10).title() == "No" or ryready.replace("!","",10).title() == "No":
                ryready = "No"
                break
            elif ryready.replace(".","",10).title() == "Yes" or ryready.replace("!","",10).title() == "Yes":
                ryready = "Yes"
                break
            else:
                ryready = "C"

print(f"Okay {Username.title()} Let's proceed! Remember always that, “If you're not prepared to be wrong, you'll never come up with anything original.” - Ken Robinson")

# Only "+" Mathematical Operator will be used on this program.
while max_info <= max_items:
    
    Qnty_1 = randrange(0,99) 
    Qnty_2 = randrange(0,99) 
    prgrm_answr = Qnty_1 + Qnty_2 
    if max_info < max_items:
        print(f"Item No.{max_info} out of {max_items}. What is {Qnty_1} + {Qnty_2}? : ")
    elif max_info == max_items:
        print(f"Item No.{max_info} out of {max_items}. What is {Qnty_1} + {Qnty_2}? : ")
    Usr_response = input("Your Answer:  ")
    if Usr_response.isalpha() == True: 
        print("The program says that you should provide a numerical input. Please try again. That answer would not be counted as an increment of your total item quiz.")
    elif Usr_response.isdigit() == True: 
        
        if int(Usr_response) == prgrm_answr: 
            correctanswer += 1
            max_info += 1
            if correctanswer == 10:
                None
            elif correctanswer >= 8 or correctanswer == 9:
                print(f"Excellent! You are indeed a smart! 🌟")
            elif correctanswer >= 5 or correctanswer == 7:
                print(f"Good Job! You are still correct! 👏")
            elif correctanswer >= 1 or correctanswer == 4:
                print(f"You got the correct answer! 👍")
        elif int(Usr_response) != prgrm_answr:
            if wronganswer == 9:
                print(f"The correct answer for Item No.{max_info} is{prgrm_answr}")
            elif wronganswer >= 7 or wronganswer == 8:
                print(f"You are still wrong! Concentrate more ! The correct answer for Item No.{max_info} is {prgrm_answr}")
            elif wronganswer >= 4 or wronganswer == 6:
                print(f"You are wrong! The correct answer for Item No.{max_info} is {prgrm_answr}")
            elif wronganswer >= 0 or wronganswer == 3:
                print(f"Incorrect 🙁 The correct answer for Item No.{max_info} is {prgrm_answr} ")
            wronganswer += 1
            max_info += 1
    elif Usr_response.isalnum() == True: 
        print("Program says that you should give a numerical input. Please try again. Your total item quiz score would not be affected by this answer..")
    else:
        print("Program says that float inputs (with . ,) or integers with decimals (with . ,) are not recognized in this Math Quiz. Please try again. Your total item quiz score would not be affected by this answer.")

#Scores and evaluation Summary.
if correctanswer >= 10 and wronganswer == 0:
    print(f"The summary of your grades would be:{correctanswer} / {max_items}.You've got a perfect score!")
elif correctanswer >= 5 or correctanswer == 9 and wronganswer >= 1:
    print(f"The summary of your grades would be: {correctanswer} / {max_items}.Great Job!")
elif correctanswer >= 1 or correctanswer == 4 and wronganswer >= 1:
    print(f"The summary of your grades would be: {correctanswer} / {max_items}. Nice try! ")
elif correctanswer == 0 and wronganswer >= 0:
    print(f"The summary of your grades would be: {correctanswer} / {max_items} Better Luck Next Time!")
