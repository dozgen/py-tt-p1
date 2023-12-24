
"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

import random




def start_game():
    attempt = 1 
    winner_num = random.randint(1, 10) 
    
    welcome = (f"""
---------------------------
Welcome to the Number Guessing Game 🤔! 
--------------------------- """)

    print (welcome)   
    while True: 
        try:
            guess_str = (input ("Pick a number between 1 and 10: ")) 
            guess = int(guess_str)
            if guess > 10 or guess < 1:
                raise ValueError ("Please enter a value in between 1 and 10.")
        except ValueError as err:
            if guess_str.isdigit() == True:
                print (f"We ran into an issue. {err}")
            else: 
                print ("Please enter value in the number form like 3 or 5.")
        else:
            if guess > winner_num:
                print ("it's lower ⬇️")
                attempt += 1
                continue
            elif guess < winner_num:
                print("it's higher ⬆️")
                attempt += 1
                continue 
            elif guess == winner_num: 
                break
    print (f"""🎊 Congratulations! 🎊 
     You got it in {attempt} attempts.🎲""")
    try: 
        answer = input("Would you like to play again? y/n ")
        if answer != "y" and answer != "n":
            raise ValueError ("please enter only y or n")
    except ValueError as err2:
        print (f"We ran into an issue. {err2}")
    else: 
        if answer.lower() == "y":
            print (f"The High Score is {attempt}")
            start_game()
        elif answer.lower() == "n":
            print ("Thanks for playing the game, see you next time!")
            
start_game()

