import random

top_of_range = input('Type a number: ') #Prompts user to enter number

if top_of_range.isdigit(): #checks if user input is a number
    top_of_range = int(top_of_range) #converts to integer if condition is true
    if top_of_range <= 0:
        print('Please type a number greater than 0 next time')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range) #prints random integer up to the number the user enters
guesses = 0

while True:
    guesses += 1 #increments guesses by 1 each time the loop runs
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess) 
    else:
        print('Please type a number next time.')
        continue #brings back to start of loop if true
    if user_guess == random_number:
        print('Your are correct!')
        break #stops loop if correct guess
    elif user_guess > random_number: #'elif' statment used to avoid using a nested if statement inside else statement15
        print('you were above the number') #if this condition is true prints this
    else:
        print('You were below the number') #if false it prints this

print(f'You got it in {guesses} guesses')