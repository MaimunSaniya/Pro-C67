import random
number = random.randrange(1, 9)
intro = "Guess a number between 1 to 10 : " 

print("---Number Guessing Game---")

play= input("Shall we start the game? ")

if(play=="yes"):
    print(intro)
elif(str(play=="no")):
    print("Ok, see you later!")



chances = 0

while(chances < 5):
    guess = int(input("Enter your guess :- "))
    chances = chances + 1

    if(guess == number):
        print("YOU WIN!! Congratulations, Very good!! If you like the game play it again (◔‿◔)")
        break
        
    if(guess<number and (guess != number-1 or guess<number+1)):
        print("Guess a number higher than ",guess)
        
    if(guess>number):
        print("Guess a number lower than ",guess)
        
    if(guess == number-1 or guess == number+1):
        print("You are very close try again")
 
if not chances < 5:
    print("YOU LOSE!! The number is ",number)

