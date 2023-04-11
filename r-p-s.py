import random

user_wins = 0       
computer_wins = 0
draws = 0
# Variables defined as 0 globally

options = ['rock', 'paper', 'scissors'] #list/data structure stored in variable 


while True: #loop for user input & quit option
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower() #converts whatever typd to lowercase
    if user_input == "q":
        break #breaks out while loop
    
    if user_input not in options: # checks for inputs not in 'options' & continues 1st loop
        continue

    random_number = random.randint(0, 2) # rock:0 paper:1 scissors:2
    computer_pick = options[random_number] #access random number of item from options variable
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors": #checks both conditions are true
        print("You Won!")
        user_wins += 1 #iterates user score by 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Its A Draw")
        draws += 1

    else :
        print("You Lost")
        computer_wins += 1 

print("You Won: ", user_wins," Times.")
print("Computer Won: ", computer_wins," Times.")
print("Draws: ", draws," Times.")
print("Goodbye")
