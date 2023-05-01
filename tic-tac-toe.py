import random # used for selecting random.choice for cpu function

board = {(0,0):" ", (0,1):" ", (0,2):" ",   # dictionary with tuples as keys & empty strings as values
         (1,0):" ", (1,1):" ", (1,2):" ",
         (2,0):" ", (2,1):" ", (2,2):" "
         }

def main(): # main game loop calls relevant functions & ends once check_win returns True or if reaches max number of turns(9)
    for i in range(9):
        usr = input("Your turn: ").split(',')
        update_user(usr)
        print_board()
        if check_win():
            print("You Win!")
            print_board()
            return
        update_cpu()
        print_board()
        if check_win():
            print("CPU Win!")
            print_board()
            return

def update_user(usr):   # takes user input & using 'map' function converts to int from string & then to tuple to access corresponding key value in board
    position = tuple(map(int,usr))  # user input converted to tuple for use with dictionary keys
    while board[position] != " ":   # continue loop if space taken
        print("Space Taken")
        usr = input("Your turn: ").split(',')
        position = tuple(map(int,usr))
    board[position] = "X" 

def update_cpu():       # create a new list of available spaces & a conditional for the cpu to add entry to a free space using random.choice
    free_space = [free for free in board.keys() if board[free] == " "] # iterates through each key of the board & assigns empty spaces to 'free' variable
    if free_space:
        free = random.choice(free_space)
        board[free] = "O"

def print_board():      # collection of print functions to represent the board visually, called after each input.
        print("-------")
        print("|" + board[0,0] + "|" + board[0,1] + "|" + board[0,2] + "|")
        print("-------")
        print("|" + board[1,0] + "|" + board[1,1] + "|" + board[1,2] + "|")
        print("-------")
        print("|" + board[2,0] + "|" + board[2,1] + "|" + board[2,2] + "|")
        print("-------", end='\n\n')

def check_win():        # loops over each row, column & diagonal directions & checks if all 3 spaces have either X or O & not empty. If True, game is won. False continues game.
    #check rows
    for i in range(3): 
        if board[(i,0)] == board[(i,1)] == board[(i,2)] != " ": 
            return True
    #check columns
    for i in range(3):
        if board[(0,i)] == board[(1,i)] == board[(2,i)] != " ":
            return True
    #check diagonals
        if board[(0,0)] == board[(1,1)] == board[(2,2)] != " ":
            return True
        if board[(0,2)] == board[(1,1)] == board[(2,0)] != " ":
            return True
    return False

main()

#   Bugs:
    #   1. Entering on full spaces should allow for another go. currently does not (Fix- swap if/else for while loop) *Fixed
    #   2. board not printng on CPU win (Fix- added print_board to check_win conditional)
    #   3. Draw shows as user win ()
    #   4. usr cells 0,1 0,2 1,0 1,2 is giving user win when should not be (Fix- typo in 2nd diagonal conditional)