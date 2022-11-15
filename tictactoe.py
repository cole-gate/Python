#import random for computer selection
import random 
#this is just to be fancy, and act like the computer is thinking
import time 

#welcomes user, didn't put into function because it only runs once
#so if user wants to play again, it doesn't welcome them again
print("Welcome to Tic Tac Toe!") 
def playerSelection():
    #ask user to select X or O and check checks if their selection is valid
    while True:
        player = input("Do you want to be X or O? ").capitalize()
        if player == "X" or player == "O":
           break
    return player

def computerSelection(player):
    #computer selects opposite of player
    if player == "X":
        return "O"
    else:
        return "X"

#made board global so it can be accessed in all functions 
#it is set as a 2D array to satisfy the requirements of the assignment
#in a 3x3 row and column grid which user has to select
# which means I don't have to pass it as a parameter constantly
board = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]

def drawBoard():
    for i in range(3):
        print(board[i])

def playerPosition(player):
    #ask user for row and column and checks if valid
    while True:
        row = int(input("Enter row (1-3):  "))
        column = int(input("Enter column (1-3): "))
        #subtract 1 from row and column because array starts at 0
        #also there's probably a better way to do this but I don't know how
        if row > 0 and row < 4 and column > 0 and column < 4 and board[row-1][column-1] == " ":
            break
        else:
            print("Unfortunately, the (", row, ",", column, ") move you have entered is not valid, please enter a new move?")
            drawBoard()
    #this bit sets the (X) or (O) in the position the user selected
    #and the board is redrawn to show the new position
    board[row-1][column-1] = player
    drawBoard()

def computerPosition(computer):
    #computer selects random position, this is the same as the playerPosition function
    #notice the index is 0-2, not 1-3
    while True:
        row = random.randint(0,2)
        column = random.randint(0,2)
    #it checks if the position is empty, if it is, it sets the position to the computer's selection
    #if not, it will continue to select a random position until it finds an empty one
        if board[row][column] == " ":
            break
    board[row][column] = computer
    print("Computer is thinking...")
    time.sleep(1)
    print("Computer selected position (", row+1, ",", column+1, ")")
    drawBoard()

#check if there is a winner, this is the easiest way I could think of
#i checked stackoverflow for help on this one but most were really complicated
#this checks through every possible winning combination and checks if the board has that combination
#it is a boolean function, so it returns true or false depending on if there is a winner, which i use in the playGame function
def winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            return True
        elif board[0][0] == board[1][1] == board[2][2] != " ":
            return True
        elif board[0][2] == board[1][1] == board[2][0] != " ":
            return True
        else:
            return False

#if there is no winner, check if board is full, if it is, the game is a tie
def fullBoard():
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

#play game function, which calls all other functions and checks for winner or tie
def playGame():
    player1 = playerSelection()
    computer1 = computerSelection(player1)
    drawBoard()
    while True:
        playerPosition(player1)
        if winner() == True:
            print("Congratulations, you won!")
            break
        elif fullBoard() == True:
            print("The game is a tie!")
            break
        computerPosition(computer1)
        if winner() == True:
            print("Sorry, you lost!")
            break
        elif fullBoard() == True:
            print("The game is a tie!")
            break
    playAgain()

#ask user if they want to play again
def playAgain():
    while True:
        playAgain = input("Do you want to play again? (Y/N) ").capitalize()
        if playAgain == "Y":
            clearBoard()
            playGame()
        elif playAgain == "N":
            print("Thanks for playing!")
            break
        else:
            print("Please enter Y or N")


# clear board to play again
# after testing I realised that the board was not being cleared
# so I had to create another little function to clear the board

def clearBoard():
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
 
playGame()
