import random

#initializing
user_score=0
computer_score=0
round=0

rps= {0:"rock", 1:"paper",2:"scissor"}

print("WELCOME TO THE ROCK, PAPER, SCISSORS GAME!")
permission= (input("Do you want to start?(y/n): ")).lower()[0]

if permission=="n":
    print("Okay, see you next time!")
    quit()
elif permission=="y":
    while True:
        number= random.randint(0,2)
        computer_guess= rps[number]
    
        user_guess= input("Please choose from rock(r), paper(p), scissors(s) or quit(q): ").lower()[0]
        
        #Printing the final score and ending the game
        if user_guess=="q":
            if computer_score>user_score:
                print("\nSorry, you lost the game!")
            elif computer_score== user_score:
                print("\nThe game was a tie!")
            else:
                print("\nCongratulations, you won!\n")
            print(f'Final Score:\n\nYour score: {user_score}. \nComputer score: {computer_score}.')
            if round>=0:
                print(f'\nYou played {round} rounds.')
            print("\nGoodbye!")
            break

        #Validating input
        elif user_guess not in["p","r","s"]:
            continue

        else:
            #Tie part
            if user_guess=="r" and computer_guess=="rock":
                print("Tie")
                print(f'Your score: {user_score}')
                print(f'Computer score: {computer_score}')
                round+=1
                print(f'Computer picked {computer_guess}')
                continue
            elif user_guess=="p" and computer_guess=="paper":
                print("Tie")
                print(f'Your score: {user_score}')
                print(f'Computer score: {computer_score}')
                round+=1
                print(f'Computer picked {computer_guess}')
                continue
            elif user_guess=="s" and computer_guess=="scissor":
                print("Tie")
                print(f'Your score: {user_score}')
                print(f'Computer score: {computer_score}')
                round+=1
                print(f'Computer picked {computer_guess}')
                continue

            #Computer wins
            elif user_guess=="r" and computer_guess=="paper":
                print("Sorry, you lost.")
                computer_score+=1
                round+=1
                print(f'Your score: {user_score}')
                print(f'Computer score: {computer_score}')
                print(f'Computer picked {computer_guess}')
                continue
            elif user_guess=="p" and computer_guess=="scissor":
                print("Sorry, you lost.")
                computer_score+=1
                print(f'Your score: {user_score}')
                print(f'Computer score: {computer_score}')
                round+=1
                print(f'Computer picked {computer_guess}')
                continue
            elif user_guess=="s" and computer_guess=="rock":
                print("Sorry, you lost.")
                computer_score+=1
                print(f'Your score: {user_score}')
                print(f'Computer score: {computer_score}')
                round+=1
                print(f'Computer picked {computer_guess}')
                continue

            #User wins
            elif user_guess=="r" and computer_guess=="scissor":
                print("You won.")
                user_score+=1
                print(f'Your score: {user_score}')
                print(f'Computer score: {computer_score}')
                round+=1
                print(f'Computer picked {computer_guess}')
                continue
            elif user_guess=="p" and computer_guess=="rock":
                print("You won.")
                user_score+=1
                print(f'Your score: {user_score}')
                print(f'Computer score: {computer_score}')
                round+=1
                print(f'Computer picked {computer_guess}')
                continue
            elif user_guess=="s" and computer_guess=="paper":
                print("You won.")
                user_score+=1
                print(f'Your score: {user_score}')
                print(f'Computer score: {computer_score}')
                round+=1
                print(f'Computer picked {computer_guess}')
                continue
        