questions = ['\nIs Python named after \'Monty Python\'?',
             'Is indentation mandatory in Python?',
             'Is Python the hardest programming language?',
             'Did Python influence the design of Java?',
             'Do pythons swallow their prey whole?']

answers = ['yes', 'yes', 'no', 'no', 'yes']

print('\n\n* * * * * * * * * * * * * * * * * * * *\nWelcome To The Python Quiz! \nPlease answer \'yes\' or \'no\' to each question.\n* * * * * * * * * * * * * * * * * * * *\n') #Welcome message before main function starts

def start(): #Function to prompt the user to start the quiz

    ready = input('Are you ready? \n')
    if ready == 'yes': #If condition is true, main function will run
        quizGame()
    else: 
        start() #loops back to start function
        
def quizGame():  #Main function for the quiz

    score = 0 #Score variable initialized with zero (declared locally withing function)

    for i in range(len(questions)): #'range defines how many times to run the loop (len). 'len' = how many items in the questions variable
        print(questions[i]) 
        ans = input('Your answer: \n') #takes answer from user & stores in variable 'ans'
        if ans == answers[i]: ## check if answer is correct by matching item in 'answers list using if statement
            print('\nCorrect!!! Well Done!\n---------------------\n') # will run if above condition is true
            score += 1 # increases score variable by 1 if correct
        else:  # code to run if condition is false
            print('\nIncorrect!!!\n************\n')

    print(f'You scored a total of: {score}!') #takes total score of answeered questions & displays in message to user
    print(f'Which is: {((score / 5) * 100)} %' )
    print('Thank You For Playing!\n')
start() #calls the first function after welcome message is displayed