print("Welcome to the quiz!")
score=0

#Asking user if he/she wants to play
user= ((input("Do you want to play the game?(y) or(n) ")).lower())[0]

#Checking input
if user!="y":
    quit()
else:
    print("Let's Play!")

quiz=input("Question 1: What does GPU stand for? ").lower()
if quiz=="graphics processing unit":
    print("Your answer is correct!")
    score+=1
else:
    print("You got the wrong answer!")

quiz=input("Question 2: What does psu stand for? ").lower()
if quiz=="power supply unit":
    print("Your answer is correct!")
    score+=1
else:
    print("You got the wrong answer!")

quiz=input("Question 3: What does cpu stand for? ").lower()
if quiz=="central processing unit":
    print("Your answer is correct!")
    score+=1
else:
    print("You got the wrong answer!")

quiz=input("Question 4: What does ram stand for? ").lower()
if quiz=="random access memory":
    print("Your answer is correct!")
    score+=1
else:
    print("You got the wrong answer!")

quiz=input("Question 5: What does rom stand for? ").lower()
if quiz=="read only memory":
    print("Your answer is correct!")
    score+=1
else:
    print("You got the wrong answer!")

quiz=input("Question 6: What does hdd stand for? ").lower()
if quiz=="hard disk drive":
    print("Your answer is correct!")
    score+=1
else:
    print("You got the wrong answer!")

quiz=input("Question 7: What does ssd stand for? ").lower()
if quiz=="solid state drive":
    print("Your answer is correct!")
    score+=1
else:
    print("You got the wrong answer!")

q1=input("Question 8: What does cmd stand for? ").lower()
if q1=="command prompt":
    print("Your answer is correct!")
    score+=1
else:
    print("You got the wrong answer!")

print(f'You scored {(score/8)*100}% which is {score} out of 8')