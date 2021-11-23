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
progintro = print("\33[32mWelcome to\33[0m \33[94m'Aleja's BrainMath Quiz!\33[0m \33[32m'This mathematics addition game will presumably examine your brain within random digits ranging from 0-99.\33[0m")
Username = input("\33[1mKindly enter you First Name below before we proceed to the Quiz:\33[0m ")
ryready = input(f"Hi \33[93m{Username.title()}\33[0m! Are you ready for the Math Quiz? \33[93m (Respond: Yes or No):\33[0m ")
Ready_ = False

# Adding Statement Conditions
while not Ready_:
    if ryready.replace(".","",10).title() == "Yes" or ryready.replace("!","",10).title() == "Yes":
        ryready = "Yes"
        Ready_ = True
    while ryready.replace(".","",10).title() != "Yes":
        if ryready.replace(".","",10).title() or ryready.replace("!","",10).title() == "No":
            ryready = input(f"\33[32mOkay, take your time\33[0m \33[93m{Username}\33[0m 😄/ Now, are you ready to start the quiz {Username}? (Respond: Yes or No):  ")
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
            if ryready.upper() in "YHJKSKLSBYWISPJKSWABMS":
                ryready = input(f"\n\033[0mPython 3.0 didn't understand your response, sorry! ☹️\nAre you now ready for the \033[32;1mMath Quiz\33[0m? (Respond: \33[34;1mYes\33[0m or \33[34;1mNo\33[0m)\n\033[32;1m>>>\33[0m\33[34;1m ")
            elif ryready.replace(".","",10).title() == "No" or ryready.replace("!","",10).title() == "No":
                ryready = "No"
                break
            elif ryready.replace(".","",10).title() == "Yes" or ryready.replace("!","",10).title() == "Yes":
                ryready = "Yes"
                break
            else:
                ryready = "C"

print(f"Okay \33[93m{Username.title()}\33[0m Let's proceed! '\33[36m\33[1m“If you're not prepared to be wrong, you'll never come up with anything original.” - Ken Robinson\33[0m")

# Only "+" Mathematical Operator will be used on this program.
while max_info <= max_items:
    
    Qnty_1 = randrange(0,99) 
    Qnty_2 = randrange(0,99) 
    prgrm_answr = Qnty_1 + Qnty_2 
    if max_info < max_items:
        print(f"Item No.{max_info} out of {max_items}. What is \33[1m\33[35m{Qnty_1}\33[0m + \33[1m\33[35m{Qnty_2}\33[0m? : ")
    elif max_info == max_items:
        print(f"Item No.{max_info} out of {max_items}. What is \33[1m\33[35m{Qnty_1}\33[0m + \33[1m\33[35m{Qnty_2}\33[0m ? : ")
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
                print(f"\33[1m\33[35mExcellent! You are indeed a smart!\33[0m🌟")
            elif correctanswer >= 5 or correctanswer == 7:
                print(f"\33[1m\33[35mGood Job! You are still correct! \33[0m 👏")
            elif correctanswer >= 1 or correctanswer == 4:
                print(f"\33[1m\33[35mYou got the correct answer!\33[0m👍")
        elif int(Usr_response) != prgrm_answr:
            if wronganswer == 9:
                print(f"The correct answer for Item No.{max_info} is \33[1m\33[32m{prgrm_answr}\33[0m")
            elif wronganswer >= 7 or wronganswer == 8:
                print(f"\33[1m\33[35mYou are still wrong!\33[0m Concentrate more ! The correct answer for Item No.{max_info} is \33[1m\33[32m{prgrm_answr}\33[0m")
            elif wronganswer >= 4 or wronganswer == 6:
                print(f"\33[1m\33[35mYou are wrong!\33[0m The correct answer for Item No.{max_info} is \33[1m\33[32m{prgrm_answr}\33[0m")
            elif wronganswer >= 0 or wronganswer == 3:
                print(f"\33[1m\33[35mIncorrect!\33[0m The correct answer for Item No.{max_info} is \33[1m\33[32m{prgrm_answr}\33[0m")
            wronganswer += 1
            max_info += 1
    elif Usr_response.isalnum() == True: 
        print("\33[31m\33[1mProgram says that you should give a numerical input. Please try again. Your total item quiz score would not be affected by this answer\33[0m.")
    else:
        print("\33[31m\33[1mProgram says that float inputs (with . ,) or integers with decimals (with . ,) are not recognized in this Math Quiz. Please try again. Your total item quiz score would not be affected by this answer.\33[0m")

#Scores and evaluation Summary.
if correctanswer >= 10 and wronganswer == 0:
    print(f"\33[36m\33[1mThe summary of your grades would be:\33[0m\\33[1m\33[37m{correctanswer} / {max_items}.\33[0m\\33[1m\33[35mYou've got a perfect score!\33[0m")
elif correctanswer >= 5 or correctanswer == 9 and wronganswer >= 1:
    print(f"\33[36m\33[1mThe summary of your grades would be:\33[0m \33[1m\33[37m{correctanswer} / {max_items}.\33[0m\\33[1m\33[35mGreat Job!\33[0m")
elif correctanswer >= 1 or correctanswer == 4 and wronganswer >= 1:
    print(f"\33[36m\33[1mThe summary of your grades would be:\33[0m \33[1m\33[37m{correctanswer} / {max_items}.\33[0m\HH\33[1m\33[35m Nice try! \33[0m")
elif correctanswer == 0 and wronganswer >= 0:
    print(f"\33[36m\33[1mThe summary of your grades would be: \33[1m\33[37m{correctanswer} / {max_items} \33[1m\33[35mBetter Luck Next Time!\33[0m")
