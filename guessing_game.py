import random

attempts=0

top_range= input("Enter the top range: ")

if top_range.isdigit():
    top_range=int(top_range)
    if top_range>0:
        pass
    else:
        print("Please try again and enter a value greater than zero next time.")
        quit()
else:
    print("Please try again and enter a number next time.")
    quit()

value= random.randint(0,top_range)

while True:
    user_input=input("Enter your guess: ")
    if user_input.isdigit():
        user_input=int(user_input)
        if user_input==value:
            print("Congratulations, you got it correct!")
            if attempts>=1:
                print(f'It took you {attempts} attempts.')
                break
            else:
                break
        elif user_input<value:
            print("Incorrect! Please try a bigger value.")
            attempts+=1
            continue
        else:
            print("Incorrect! Please try a smaller value")
            attempts+=1
            continue
    else:
        print("Please enter a valid input and try again!")
        break
    
